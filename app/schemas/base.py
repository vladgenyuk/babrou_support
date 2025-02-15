from typing import Generic, List, TypeVar

from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)


T = TypeVar("T")


class BasePaginatedResponse(BaseSchema, Generic[T]):
    items: List[T]
    total_items: int
    total_pages: int
    page: int
    page_size: int


# add prev page and next page.
