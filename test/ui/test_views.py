from django.test import TestCase
from django.urls import reverse
from db.models import ProductModel


class TestProductView(TestCase):

    def setUp(self):
        self.url = reverse("product")

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("form", response.context)
        self.assertTemplateUsed(response, "ui/product.html")
    
    def test_post_creates_product(self):
        response = self.client.post(self.url, dict(name="Product", price=500))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ProductModel.objects.count(), 1)
