from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, EmailStr
from typing import Dict

app = FastAPI()

class Contact(BaseModel):
    name: str
    phone: str
    email: EmailStr

# In-memory database
contacts: Dict[str, Contact] = {}

@app.post("/contacts/")
def add_contact(contact: Contact):
    if contact.name in contacts:
        raise HTTPException(status_code=400, detail="Contact already exists.")
    contacts[contact.name] = contact
    return {"message": f"Contact '{contact.name}' added."}


@app.get("/contacts/")
def search_contact(name: str = Query(...)):
    contact = contacts.get(name)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found.")
    return contact

@app.post("/contacts/{name}")
def update_contact(name: str, updated: Contact):
    if name not in contacts:
        raise HTTPException(status_code=404, detail="Contact not found.")
    contacts[name] = updated
    return {"message": f"Contact '{name}' updated."}

@app.delete("/contacts/{name}")
def delete_contact(name: str):
    if name not in contacts:
        raise HTTPException(status_code=404, detail="Contact not found.")
    del contacts[name]
    return {"message": f"Contact '{name}' deleted."}

