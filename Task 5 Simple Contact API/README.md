# Simple Contact API

A lightweight FastAPI app to manage contact info in-memory.

## Features

- Add a contact
- Search by name using query parameter
- Update and delete using path parameters

## Endpoints

- `POST /contacts/`
- `GET /contacts/?name=John`
- `POST /contacts/John`
- `DELETE /contacts/John`

## Run

```bash
uvicorn main:app --reload
