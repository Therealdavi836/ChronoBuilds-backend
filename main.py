from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import characters, builds

app = FastAPI()

# 1. DEFINE MIDDLEWARE FIRST
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. INCLUDE ROUTERS SECOND
app.include_router(characters.router, prefix="/api")
app.include_router(builds.router, prefix="/api/builds")

@app.get("/")
def read_root():
    return {"message": "Backend funcionando"}

from database import engine, Base
from models import character, build, weapon, artifact # Import ALL models here

# This line creates the tables if they don't exist
Base.metadata.create_all(bind=engine)