from app.crud.base import CrudBase
from app.models import Order
from app.schemas.order import OrderSchema


class CrudOrder(CrudBase):
    pass


order_crud: CrudOrder = CrudOrder(Order, OrderSchema)
