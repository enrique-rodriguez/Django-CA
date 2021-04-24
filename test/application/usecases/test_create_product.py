from unittest import TestCase
from unittest.mock import Mock
from app.usecases.create_product import CreateProduct


class TestCreateProduct(TestCase):

    def setUp(self):
        self.product_repo = Mock()
        self.create_product = CreateProduct(
            product_repo=self.product_repo,
        )

    def test_product_created(self):
        request = dict(name="My Product", price=500)
        self.create_product.execute(request)
        self.assertTrue(self.product_repo.save.called)
