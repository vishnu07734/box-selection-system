from django import forms
from .models import Product, Box, Order, OrderItem


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "length_cm", "width_cm", "height_cm", "weight_kg"]


class BoxForm(forms.ModelForm):
    class Meta:
        model = Box
        fields = ["name", "length_cm", "width_cm", "height_cm", "max_weight_kg", "cost"]


class OrderCreateForm(forms.Form):
    products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        help_text="Select the products to include. Set quantities after creating the order in admin."
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["products"].queryset = Product.objects.all()


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ["product", "quantity"]
