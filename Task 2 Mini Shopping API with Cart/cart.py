import json
from typing import List
from math import ceil
from pathlib import Path

CART_FILE = Path("cart_data.json")
PRODUCT_FILE = Path("products.json")

def load_cart() -> List[dict]:
    if not CART_FILE.exists():
        return []
    try:
        with open(CART_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_cart(cart: List[dict]):
    with open(CART_FILE, "w") as f:
        json.dump(cart, f, indent=4)

def load_products() -> List[dict]:
    with open(PRODUCT_FILE, "r") as f:
        return json.load(f)

def add_to_cart(product_id: int, qty: int) -> str:
    cart = load_cart()
    products = load_products()

    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        return "Product not found."

    existing = next((item for item in cart if item["id"] == product_id), None)
    if existing:
        existing["quantity"] += qty
    else:
        cart.append({
            "id": product["id"],
            "name": product["name"],
            "price": product["price"],
            "quantity": qty
        })

    save_cart(cart)
    return f"Added {qty} x {product['name']} to cart."

def checkout_cart() -> dict:
    cart = load_cart()
    if not cart:
        return {"message": "Cart is empty."}

    total = sum(item["price"] * item["quantity"] for item in cart)
    total_rounded = round(total, 2)

    return {
        "items": cart,
        "total": total_rounded
    }
