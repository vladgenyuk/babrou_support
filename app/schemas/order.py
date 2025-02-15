from datetime import datetime

from pydantic import Field

from .base import BaseSchema


class OrderSchemaCreate(BaseSchema):
    pass


class OrderSchema(OrderSchemaCreate):
    id: int = Field(..., gt=0)
    created_at: datetime | None = Field(None)


# field(default = None)
