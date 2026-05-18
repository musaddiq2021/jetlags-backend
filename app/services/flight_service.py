from app.services.providers.mock_provider import get_mock_live_flights

def get_live_flights_service():
    flights = get_mock_live_flights()

    return {
        "status": "ok",
        "source": "mock-provider",
        "count": len(flights),
        "flights": flights
    }