from fastapi import APIRouter
from app.services.flight_service import get_mock_live_flights

router = APIRouter()

@router.get("/flights/live")
def get_live_flights():
    flights = get_mock_live_flights()

    return {
        "status": "ok",
        "source": "mock-data",
        "count": len(flights),
        "flights": flights
    }