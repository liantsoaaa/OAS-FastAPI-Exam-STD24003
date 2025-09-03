from fastapi import FastAPI, Response #type: ignore
from fastapi.responses import PlainTextResponse # type: ignore
from pydantic import BaseModel # type: ignore
from typing import List
from fastapi import HTTPException # type: ignore

app = FastAPI()

class Characteristic(BaseModel):
    ram_memory: int 
    rom_memory: int

class Phone(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: Characteristic

phone_db: List[Phone] = []

#a
@app.get("/health")
async def health():
    return PlainTextResponse("OK", status_code=200)


#b
@app.post("/phones", status_code=201)
async def create_phone(phone: Phone):
    phone_db.append(phone)
    return phone

#c
@app.get("/phones", response_model=List[Phone])
async def get_phones():
    return phone_db

#d
@app.get("/phones/{phone_id}", response_model=Phone)
async def get_phone(phone_id: str):
    for phone in phone_db:
        if phone.identifier == phone_id:
            return phone
    raise HTTPException(status_code=404, detail=f"Phone with '{phone_id}' not found")


#e BONUS
@app.put("/phones/{phone_id}/characteristics", response_model=Phone)
async def update_phone_characteristics(phone_id: str, characteristics: Characteristic):
    for phone in phone_db:
        if phone.identifier == phone_id:
            phone.characteristics = characteristics
            return phone
    raise HTTPException(status_code=404, detail=f"Phone with '{phone_id}' not found")

