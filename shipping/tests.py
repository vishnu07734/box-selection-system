from decimal import Decimal
from django.test import TestCase
from .models import Product, Box, Order, OrderItem
from .packing import pack_items, recommend_box, Item


class PackingAlgorithmTests(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Keyboard", length_cm=20, width_cm=15, height_cm=5, weight_kg=1
        )

    def make_box(self, name, l, w, h, max_weight=10, cost=10):
        return Box.objects.create(
            name=name, length_cm=l, width_cm=w, height_cm=h,
            max_weight_kg=max_weight, cost=cost
        )

    def test_recommends_cheapest_box_that_fits(self):
        cheap = self.make_box("Small", 22, 17, 7, cost=12)
        self.make_box("Large", 30, 25, 15, cost=25)
        chosen, checks = recommend_box([(self.product, 1)], Box.objects.all())
        self.assertEqual(chosen, cheap)
        self.assertEqual(len([c for c in checks if c["eligible"]]), 2)

    def test_rejects_weight_over_capacity(self):
        box = self.make_box("Light", 25, 20, 10, max_weight=Decimal("0.5"))
        chosen, checks = recommend_box([(self.product, 1)], [box])
        self.assertIsNone(chosen)
        self.assertFalse(checks[0]["eligible"])
        self.assertIn("weight", checks[0]["reasons"][0].lower())

    def test_rejects_dimensions_that_do_not_fit(self):
        box = self.make_box("Tiny", 10, 10, 10)
        chosen, checks = recommend_box([(self.product, 1)], [box])
        self.assertIsNone(chosen)
        self.assertFalse(checks[0]["eligible"])

    def test_checks_rotation(self):
        item = Item("rotated", Decimal("10"), Decimal("20"), Decimal("5"), Decimal("1"))
        placements = pack_items([item], Decimal("20"), Decimal("10"), Decimal("5"))
        self.assertIsNotNone(placements)

    def test_multiple_products_are_not_allowed_to_overlap(self):
        item = Item("unit", Decimal("5"), Decimal("5"), Decimal("5"), Decimal("1"))
        placements = pack_items([item, item], Decimal("5"), Decimal("5"), Decimal("10"))
        self.assertIsNotNone(placements)
        self.assertNotEqual(
            (placements[0].x, placements[0].y, placements[0].z),
            (placements[1].x, placements[1].y, placements[1].z),
        )

    def test_order_weight_is_aggregated(self):
        box = self.make_box("Capacity", 50, 50, 50, max_weight=Decimal("1.5"))
        chosen, _ = recommend_box([(self.product, 2)], [box])
        self.assertIsNone(chosen)

    def test_no_boxes_returns_no_recommendation(self):
        chosen, checks = recommend_box([(self.product, 1)], [])
        self.assertIsNone(chosen)
        self.assertEqual(checks, [])


class WebFlowTests(TestCase):
    def test_dashboard_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_product_can_be_created_from_form(self):
        response = self.client.post("/products/", {
            "name": "Mouse", "length_cm": "10", "width_cm": "8",
            "height_cm": "4", "weight_kg": "0.2"
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Product.objects.filter(name="Mouse").exists())
