from app.entities import Product


class CreateProduct:

    def __init__(self, product_repo):
        self.product_repo = product_repo

    def execute(self, request):
        product = Product(**request)
        self.product_repo.save(product)
