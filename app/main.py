from fastapi import FastAPI
from app.api.flights import router as flights_router
from app.api.dashboard import router as dashboard_router

app = FastAPI(
    title="Jetlags Backend API",
    description="Backend API for Jetlags aviation disruption intelligence platform",
    version="0.1.0"
)

app.include_router(flights_router, prefix="/api")
app.include_router(dashboard_router, prefix="/api")

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

