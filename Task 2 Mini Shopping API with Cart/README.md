# Mini Shopping API with Cart

A simple FastAPI-based shopping cart system.

## Features

- Browse products
- Add products to cart
- Checkout total amount

## Endpoints

- `GET /products/`
- `POST /cart/add?product_id=1&qty=2`
- `GET /cart/checkout`

## Tech

- FastAPI
- Python
- JSON storage

## Run

```bash
uvicorn main:app --reload
