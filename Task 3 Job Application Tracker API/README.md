# Job Application Tracker API

A FastAPI-based API to track and search job applications.

## Features

- Add new job applications
- List all applications
- Search by status (pending, accepted, rejected)

## Endpoints

- `POST /applications/`
- `GET /applications/`
- `GET /applications/search?status=pending`

## Run

```bash
uvicorn main:app --reload
