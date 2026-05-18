from fastapi import FastAPI
from app.api.flights import router as flights_router
from app.api.dashboard import router as dashboard_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Jetlags Backend API",
    description="Backend API for Jetlags aviation disruption intelligence platform",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://jetlags.uk"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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

