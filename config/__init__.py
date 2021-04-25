from app import usecases
from config import settings
from utils import import_string


class AppConfig:
    
    @property
    def create_product(self):
        return usecases.CreateProduct(
            product_repo=import_string(settings.STORAGE.get("product")),
        )