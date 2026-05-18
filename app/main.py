from fastapi import FastAPI

app = FastAPI(
    title="Jetlags Backend API",
    description="Backend API for Jetlags aviation disruption intelligence platform",
    version="0.1.0"
)

@app.get("/")
def home():
    return {
        "message": "Jetlags Backend is running",
        "status": "ok"
    }

@app.get("/api/health")
def health_check():
    return {
        "status": "ok",
        "service": "Jetlags Backend API"
    }

#FALSE DATRA ENDPOINT
@app.get("/api/flights/live")
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