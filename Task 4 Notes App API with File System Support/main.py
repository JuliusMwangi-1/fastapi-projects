from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from pathlib import Path

app = FastAPI()
NOTES_DIR = Path("notes")
NOTES_DIR.mkdir(exist_ok=True)

class NoteContent(BaseModel):
    content: str

def get_note_path(title: str) -> Path:
    return NOTES_DIR / f"{title}.txt"

@app.post("/notes/")
def create_note(title: str, note: NoteContent):
    try:
        file_path = get_note_path(title)
        if file_path.exists():
            raise HTTPException(status_code=400, detail="Note already exists.")
        with open(file_path, "w") as f:
            f.write(note.content)
        return {"message": f"Note '{title}' created."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/notes/{title}")
def read_note(title: str):
    try:
        file_path = get_note_path(title)
        if not file_path.exists():
            raise HTTPException(status_code=404, detail="Note not found.")
        with open(file_path, "r") as f:
            content = f.read()
        return {"title": title, "content": content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/notes/{title}")
def update_note(title: str, note: NoteContent):
    try:
        file_path = get_note_path(title)
        if not file_path.exists():
            raise HTTPException(status_code=404, detail="Note not found.")
        with open(file_path, "w") as f:
            f.write(note.content)
        return {"message": f"Note '{title}' updated."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/notes/{title}")
def delete_note(title: str):
    try:
        file_path = get_note_path(title)
        if not file_path.exists():
            raise HTTPException(status_code=404, detail="Note not found.")
        file_path.unlink()
        return {"message": f"Note '{title}' deleted."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
