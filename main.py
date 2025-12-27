from fastapi import FastAPI
from routers import characters
from fastapi.middleware.cors import CORSMiddleware
from routers import builds

app = FastAPI()

# Include routers
app.include_router(characters.router, prefix="/api")

# Include builds router
app.include_router(builds.router, prefix="/api/builds")

@app.get("/")
def read_root():
    return {"message": "Backend funcionando"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], # Allow your Next.js app
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)