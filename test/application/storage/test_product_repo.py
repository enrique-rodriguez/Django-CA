from django.test import TestCase
from app.storage import ProductRepo
from app.entities import Product


class TestProductRepo(TestCase):

    def setUp(self):
        self.product_repo = ProductRepo()

    def test_save_product(self):
        product = Product(name="Name", price=500)
        self.product_repo.save(product)
        self.assertEqual(product.id, 1)
