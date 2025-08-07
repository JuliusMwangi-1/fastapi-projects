from fastapi import FastAPI, HTTPException, Query
from models import JobApplication
from file_handler import load_applications, save_applications

app = FastAPI()
db = load_applications()

@app.post("/applications/")
def add_application(app_data: JobApplication):
    try:
        db.append(app_data.dict())
        save_applications(db)
        return {"message": "Application added successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/applications/")
def list_applications():
    try:
        return db
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/applications/search")
def search_applications(status: str = Query(...)):
    try:
        filtered = [app for app in db if app["status"].lower() == status.lower()]
        return filtered
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
