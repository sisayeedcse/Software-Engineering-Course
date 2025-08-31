from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: int
    qnt: int

products: List[Product] = []

api = FastAPI()

@api.get("/")
def home():
    return {"message": "Welcome to my Inventory"}

@api.get("/get")
def get_products():
    return products

@api.get("/get/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    return {"message": "Product not found"}

@api.post("/post")
def post_product(product: Product):
    products.append(product)
    return {"message": "Product added successfully", "product": product}

@api.put("/put/{product_id}")
def update_product(product_id: int, updated_product: Product):
    for index, product in enumerate(products):
        if product.id == product_id:
            products[index] = updated_product
            return {"message": "Product updated successfully", "product": updated_product}
    return {"message": "Product not found for update"}

@api.delete("/delete/{product_id}")
def delete_product(product_id: int):
    for index, product in enumerate(products):
        if product.id == product_id:
            deleted = products.pop(index)
            return {"message": "Product deleted successfully", "product": deleted}
    return {"message": "Product not found for deletion"}
