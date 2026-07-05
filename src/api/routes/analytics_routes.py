from fastapi import APIRouter

from src.analytics.analytics_manager import (
    AnalyticsManager
)

router = APIRouter()

analytics_manager = AnalyticsManager()


@router.get("/dashboard")
def get_dashboard():

    return (
        analytics_manager.get_dashboard()
    )