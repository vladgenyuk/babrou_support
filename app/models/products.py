from sqlalchemy import DECIMAL, TIMESTAMP, BigInteger, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base


class Product(Base):
    __tablename__ = "products"
    # from tiping import Optional -> Mapped[Optional[int]]
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    created_at: Mapped[TIMESTAMP | None] = mapped_column(TIMESTAMP, nullable=True, default=func.now())
    product_name: Mapped[str | None] = mapped_column(String(100), nullable=True)
    price: Mapped[int | None] = mapped_column(DECIMAL(15, 2), nullable=True)
    cost: Mapped[int | None] = mapped_column(DECIMAL(15, 2), nullable=True)
    stock: Mapped[int | None] = mapped_column(Integer, nullable=True)

    orders_products = relationship("OrdersProducts", back_populates="products")


# index prod name
# __rw_fields__ =(...)
