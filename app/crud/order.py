from datetime import datetime
from typing import List

from sqlalchemy import text, select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CrudBase, S
from app.models import Order, Product, OrdersProducts
from app.schemas.order import OrderReturnSchema


class CrudOrder(CrudBase):
    async def get_by_id(self, session: AsyncSession, id: int) -> S | None:
        query = (
            select(
                Order.id.label("order_id"),
                Order.created_at.label("order_created_at"),
                func.json_agg(
                    func.jsonb_build_object(
                        "product_id", Product.id,
                        "product_name", Product.product_name,
                        "amount", OrdersProducts.amount,
                        "price", Product.price,
                        "cost", Product.cost
                    )
                ).label("products")
            )
            .join(OrdersProducts, Order.id == OrdersProducts.order_id)
            .join(Product, OrdersProducts.product_id == Product.id)
            .filter(Order.id == id)
            .group_by(Order.id, Order.created_at)
        )

        result = await session.execute(query)
        return result.mappings().first() if result else {}

    async def create_order(
            self,
            session: AsyncSession,
            create_obj
    ) -> int:
        """
        Creates an order and associated order products in the database.

        Args:
            session: The async database session.
            product_ids: List of product IDs.
            amounts: List of amounts corresponding to each product.
            order_created_at: Timestamp for the order creation.

        Returns:
            The ID of the newly created order.
        """
        if len(create_obj.product_ids) != len(create_obj.amounts):
            raise ValueError("The lengths of product_ids and amounts must match.")

        call_function_stmt = text("""
            SELECT create_order_with_products(
                :product_ids, 
                :amounts, 
                :order_created_at
            ) AS order_id;
        """)

        result = await session.execute(
            call_function_stmt,
            {
                "product_ids": create_obj.product_ids,
                "amounts": create_obj.amounts,
                "order_created_at": datetime.now()
            }
        )

        order_id = result.scalar()
        return order_id


order_crud: CrudOrder = CrudOrder(Order, OrderReturnSchema)