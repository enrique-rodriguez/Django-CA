from config import AppConfig
from db.forms import ProductForm
from django.views.generic import FormView
from django.forms import models as model_forms


class ProductView(FormView, AppConfig):
    template_name = "ui/product.html"
    form_class = ProductForm
    success_url = '/'

    def form_valid(self, form):
        self.create_product.execute(form.cleaned_data)
        return super().form_valid(form)

product = ProductView.as_view()