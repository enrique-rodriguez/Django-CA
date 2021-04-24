from django.test import TestCase
from django.urls import reverse, resolve
from ui import views

class TestUrls(TestCase):

    def assertUrlResolves(self, url, view):
        self.assertEqual(resolve(url).func, view)

    def test_product_url(self):
        self.assertUrlResolves(reverse("product"), views.product)
        