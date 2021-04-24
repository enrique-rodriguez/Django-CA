from django import forms
from db import models


class ProductForm(forms.ModelForm):
    class Meta:
        model = models.ProductModel
        fields = '__all__'