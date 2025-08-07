from fastapi import FastAPI, Query
from cart import load_products, add_to_cart, checkout_cart

app = FastAPI()

@app.get("/products/")
def list_products():
    try:
        return load_products()
    except Exception as e:
        return {"error": str(e)}

@app.post("/cart/add")
def add_item(product_id: int = Query(...), qty: int = Query(1)):
    try:
        message = add_to_cart(product_id, qty)
        return {"message": message}
    except Exception as e:
        return {"error": str(e)}

@app.get("/cart/checkout")
def checkout():
    try:
        return checkout_cart()
    except Exception as e:
        return {"error": str(e)}
