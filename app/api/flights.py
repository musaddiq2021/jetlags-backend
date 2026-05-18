from fastapi import APIRouter

router = APIRouter()

@router.get("/flights/live")
def get_live_flights():
    return {
        "status": "ok",
        "source": "mock-data",
        "flights": [
            {
                "flight": "EK001",
                "route": "DXB → LHR",
                "status": "Delayed",
                "delay": "+48m",
                "risk": "High"
            },
            {
                "flight": "EK215",
                "route": "DXB → LAX",
                "status": "On Time",
                "delay": "—",
                "risk": "Low"
            },
            {
                "flight": "BA142",
                "route": "DEL → LHR",
                "status": "Monitoring",
                "delay": "+20m",
                "risk": "Medium"
            }
        ]
    }