from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.midlewares.db import DBSessionMiddleware
from app.routers.order import order_router
from app.routers.order_product import order_product_router
from app.routers.product import product_router


app = FastAPI()
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
)


app.include_router(order_router, tags=["Orders"])
app.include_router(order_product_router, tags=["OrdersProducts"])
app.include_router(product_router, tags=["Products"])


app.add_middleware(DBSessionMiddleware)


@app.get("/")
async def hello_world():
    return {"message": "Hello, World!"}
