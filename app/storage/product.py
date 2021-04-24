from db.models import ProductModel


class ProductRepo:
    
    def save(self, product):
        data = vars(product)
        model = ProductModel.objects.create(**data)
        product.id = model.id