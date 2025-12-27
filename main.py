from fastapi import FastAPI
from routers import characters

app = FastAPI()

app.include_router(characters.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Backend funcionando"}
