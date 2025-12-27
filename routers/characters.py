from fastapi import APIRouter
from services.external_api import fetch_characters_from_api

router = APIRouter()

@router.get("/characters")
def get_characters():
    characters = fetch_characters_from_api()
    return {"characters": characters}