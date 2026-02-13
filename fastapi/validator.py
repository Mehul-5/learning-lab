from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

app = FastAPI()

class Case(BaseModel):
    case_id: int
    suspect_name: str
    priority: int = 1

@app.post("/case", response_model=Case)
def case_detail(cases:Case):
    return cases

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
