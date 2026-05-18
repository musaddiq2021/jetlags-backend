from fastapi import APIRouter
from app.services.flight_service import (
    get_live_flights_service,
    get_uk_live_flights_service
)

router = APIRouter()


@router.get("/flights/live")
def get_live_flights():
    return get_live_flights_service()


@router.get("/flights/live/uk")
def get_uk_live_flights():
    return get_uk_live_flights_service()