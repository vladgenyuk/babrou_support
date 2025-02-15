from datetime import datetime

from pydantic import Field

from .base import BaseSchema


class OrderProductsSchemaCreate(BaseSchema):
    order_id: int | None = Field(default=None, ge=0)
    product_id: int | None = Field(None, ge=0)
    amount: int | None = Field(None, ge=0)


# field(default = None)


class OrderProductsSchema(OrderProductsSchemaCreate):
    id: int = Field(..., gt=0)
    created_at: datetime | None = Field(None)
