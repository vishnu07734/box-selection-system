from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .forms import ProductForm, BoxForm, OrderCreateForm
from .models import Product, Box, Order, OrderItem
from .packing import recommend_box


def dashboard(request):
    return render(request, "shipping/dashboard.html", {
        "product_count": Product.objects.count(),
        "box_count": Box.objects.count(),
        "order_count": Order.objects.count(),
        "recent_orders": Order.objects.order_by("-created_at")[:5],
    })


def product_list(request):
    form = ProductForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Product added.")
        return redirect("product_list")
    return render(request, "shipping/product_list.html", {
        "products": Product.objects.all(), "form": form
    })


@require_POST
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    try:
        product.delete()
        messages.success(request, "Product deleted.")
    except Exception:
        messages.error(request, "This product is used by an order and cannot be deleted.")
    return redirect("product_list")


def box_list(request):
    form = BoxForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Shipping box added.")
        return redirect("box_list")
    return render(request, "shipping/box_list.html", {
        "boxes": Box.objects.all(), "form": form
    })


@require_POST
def box_delete(request, pk):
    get_object_or_404(Box, pk=pk).delete()
    messages.success(request, "Shipping box deleted.")
    return redirect("box_list")


def order_create(request):
    form = OrderCreateForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        order = Order.objects.create()
        for product in form.cleaned_data["products"]:
            OrderItem.objects.create(order=order, product=product, quantity=1)
        messages.success(request, f"Order #{order.pk} created. You can adjust quantities in Django admin.")
        return redirect("order_detail", pk=order.pk)
    return render(request, "shipping/order_create.html", {"form": form})


def order_detail(request, pk):
    order = get_object_or_404(Order.objects.prefetch_related("order_items__product"), pk=pk)
    recommendation, box_checks = recommend_box(
        [(line.product, line.quantity) for line in order.order_items.all()],
        Box.objects.all(),
    )
    total_weight = sum(
        (line.product.weight_kg * line.quantity for line in order.order_items.all()),
        start=0,
    )
    return render(request, "shipping/order_detail.html", {
        "order": order, "recommendation": recommendation,
        "box_checks": box_checks, "total_weight": total_weight,
    })
