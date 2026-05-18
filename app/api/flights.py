from fastapi import APIRouter
from app.services.flight_service import get_live_flights_service

router = APIRouter()

@router.get("/flights/live")
def get_live_flights():
    return get_live_flights_service()