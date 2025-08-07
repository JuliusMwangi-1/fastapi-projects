import json
from typing import List, Dict
from models import Student
from pathlib import Path

FILE_PATH = Path("students.json")

def load_students() -> List[Dict]:
    if not FILE_PATH.exists():
        return []
    try:
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_students(students: List[Dict]):
    with open(FILE_PATH, "w") as f:
        json.dump(students, f, indent=4)

def compute_average_and_grade(subject_scores: Dict[str, float]) -> (float, str):
    avg = sum(subject_scores.values()) / len(subject_scores)
    
    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    elif avg >= 60:
        grade = "D"
    else:
        grade = "F"

    return round(avg, 2), grade
