from decimal import Decimal
from django.core.management.base import BaseCommand
from shipping.models import Product, Box


class Command(BaseCommand):
    help = "Create a small demo catalogue (safe to run more than once)."

    def handle(self, *args, **options):
        products = [
            ("Keyboard", "20", "15", "5", "1.000"),
            ("Mouse", "10", "7", "4", "0.200"),
            ("Notebook", "21", "15", "2", "0.350"),
        ]
        boxes = [
            ("Small carton", "25", "20", "12", "5.000", "18.00"),
            ("Medium carton", "35", "25", "18", "10.000", "28.00"),
            ("Large carton", "45", "35", "25", "20.000", "45.00"),
        ]
        for name, l, w, h, weight in products:
            Product.objects.update_or_create(name=name, defaults={
                "length_cm": Decimal(l), "width_cm": Decimal(w),
                "height_cm": Decimal(h), "weight_kg": Decimal(weight),
            })
        for name, l, w, h, max_weight, cost in boxes:
            Box.objects.update_or_create(name=name, defaults={
                "length_cm": Decimal(l), "width_cm": Decimal(w),
                "height_cm": Decimal(h), "max_weight_kg": Decimal(max_weight),
                "cost": Decimal(cost),
            })
        self.stdout.write(self.style.SUCCESS("Demo products and boxes are ready."))
