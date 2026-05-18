from app.services.providers.opensky_provider import (
    get_opensky_live_flights,
    get_opensky_uk_live_flights
)
from app.services.providers.mock_provider import get_mock_live_flights


def get_live_flights_service():
    try:
        flights = get_opensky_live_flights()

        return {
            "status": "ok",
            "source": "opensky",
            "region": "global",
            "count": len(flights),
            "flights": flights
        }

    except Exception as error:
        flights = get_mock_live_flights()

        return {
            "status": "ok",
            "source": "mock-provider",
            "region": "global",
            "fallback_used": True,
            "reason": str(error),
            "count": len(flights),
            "flights": flights
        }


def get_uk_live_flights_service():
    try:
        flights = get_opensky_uk_live_flights()

        return {
            "status": "ok",
            "source": "opensky",
            "region": "uk",
            "count": len(flights),
            "flights": flights
        }

    except Exception as error:
        flights = get_mock_live_flights()

        return {
            "status": "ok",
            "source": "mock-provider",
            "region": "uk",
            "fallback_used": True,
            "reason": str(error),
            "count": len(flights),
            "flights": flights
        }