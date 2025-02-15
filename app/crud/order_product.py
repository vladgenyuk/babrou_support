from app.crud.base import CrudBase
from app.models.orders_products import OrdersProducts
from app.schemas.order_product import OrderProductsSchema


class CrudOrderProduct(CrudBase):
    pass


orders_products_crud: CrudOrderProduct = CrudOrderProduct(OrdersProducts, OrderProductsSchema)
