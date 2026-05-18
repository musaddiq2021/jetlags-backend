from fastapi import APIRouter
from app.services.dashboard_service import get_dashboard_overview_service

router = APIRouter()


@router.get("/dashboard/overview")
def get_dashboard_overview():
    return get_dashboard_overview_service()