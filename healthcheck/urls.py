from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HealthCheckView, ProcessTextView, SampleModelViewSet

router = DefaultRouter()
router.register(r"sample", SampleModelViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("health/", HealthCheckView.as_view(), name="health_check"),
    path("process-text/", ProcessTextView.as_view(), name="process_text"),
]