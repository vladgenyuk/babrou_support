from app.crud.base import CrudBase
from app.models import Product
from app.schemas.product import ProductSchema


class CrudProduct(CrudBase):
    pass


product_crud: CrudProduct = CrudProduct(Product, ProductSchema)
