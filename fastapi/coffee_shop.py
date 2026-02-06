from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4

app = FastAPI()

class Coffee(BaseModel):
    id: Optional[UUID] = None
    name: str

menu = ["latte", "expresso", "cold coffee"]

@app.get("/menu", response_model=List[str])
def read_menu():
    return menu

@app.post("/menu/", response_model=Coffee)
def order(coffee: Coffee):
    if coffee.name.lower() not in menu:
        raise HTTPException(status_code=404, detail="Coffee not available")
    
    coffee.id = uuid4()
    return coffee

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
