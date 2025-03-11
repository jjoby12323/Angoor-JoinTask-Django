from django.urls import path
from .views import HealthCheckView, ProcessTextView

urlpatterns = [
    path("health/", HealthCheckView.as_view(), name="health_check"),
    path("process-text/", ProcessTextView.as_view(), name="process_text"),
]