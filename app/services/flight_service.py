from app.services.providers.opensky_provider import get_opensky_live_flights
from app.services.providers.mock_provider import get_mock_live_flights

def get_live_flights_service():
    try:
        flights = get_opensky_live_flights()

        return {
            "status": "ok",
            "source": "opensky",
            "count": len(flights),
            "flights": flights
        }

    except Exception as error:
        flights = get_mock_live_flights()

        return {
            "status": "ok",
            "source": "mock-provider",
            "fallback_used": True,
            "reason": str(error),
            "count": len(flights),
            "flights": flights
        }