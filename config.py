from app import (
    usecases,
    storage,
)


class AppConfig:
    
    @property
    def create_product(self):
        return usecases.CreateProduct(
            product_repo=storage.product_repo,
        )