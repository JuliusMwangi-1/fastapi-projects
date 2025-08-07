from fastapi import FastAPI, HTTPException
from models import Student
from utils import load_students, save_students, compute_average_and_grade

app = FastAPI()
students_db = load_students()

@app.post("/students/")
def add_student(student: Student):
    try:
        for s in students_db:
            if s["name"].lower() == student.name.lower():
                raise HTTPException(status_code=400, detail="Student already exists.")
        
        avg, grade = compute_average_and_grade(student.subject_scores)
        student.average = avg
        student.grade = grade

        students_db.append(student.dict())
        save_students(students_db)
        return {"message": "Student added successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/students/{name}")
def get_student(name: str):
    try:
        for s in students_db:
            if s["name"].lower() == name.lower():
                return s
        raise HTTPException(status_code=404, detail="Student not found.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/students/")
def get_all_students():
    try:
        return students_db
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
