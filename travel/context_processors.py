"""Expose reusable travel context values."""
from .models import Trip


def travel_globals(request):
    """Small helper values reused in layout templates."""
    if request.user.is_authenticated:
        recent_trips = Trip.objects.filter(user=request.user).order_by("-created_at")[:4]
    else:
        recent_trips = []
    return {
        "nav_recent_trips": recent_trips,
    }
