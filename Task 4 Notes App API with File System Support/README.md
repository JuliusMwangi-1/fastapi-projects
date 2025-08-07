  # Notes App API (File-Based)

A FastAPI app to manage notes saved as individual `.txt` files.

## Features

- Create notes
- Read notes
- Update notes
- Delete notes

## Endpoints

- `POST /notes/?title=MyNote`
- `GET /notes/MyNote`
- `POST /notes/MyNote` (update)
- `DELETE /notes/MyNote`

## Tech

- FastAPI
- Python
- OS + Pathlib modules
- File system storage

## Run

```bash
uvicorn main:app --reload
  