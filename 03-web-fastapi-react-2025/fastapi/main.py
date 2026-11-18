from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "selamun aleykum dünya"}

class Car(BaseModel):
    brand: int
    year: int
    price: float

@app.post("/cars/")
async def create_car(car: Car):
    return car
