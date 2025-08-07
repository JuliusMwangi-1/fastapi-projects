from pydantic import BaseModel

class JobApplication(BaseModel):
    name: str
    company: str
    position: str
    status: str  # e.g., "pending", "accepted", "rejected"
