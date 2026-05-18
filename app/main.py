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