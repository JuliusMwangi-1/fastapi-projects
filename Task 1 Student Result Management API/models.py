from typing import Dict
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    subject_scores: Dict[str, float]
    average: float = 0.0
    grade: str = ""
