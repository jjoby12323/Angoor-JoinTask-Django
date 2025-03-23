from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .tasks import health_check_task, process_text_task
from .models import SampleModel
from .serializers import SampleModelSerializer


class SampleModelViewSet(viewsets.ModelViewSet):
    queryset = SampleModel.objects.all()
    serializer_class = SampleModelSerializer

class HealthCheckView(APIView):
    """Health check API to verify the Django app and Celery worker"""

    def get(self, request):
        task_result = health_check_task.delay()
        return Response({"Status": "Healthy", "celery_task_id": task_result.id}, status=status.HTTP_200_OK)

class ProcessTextView(APIView):
    """API to trigger a background text processing task"""

    def post(self, request):
        text = request.data.get("text")

        if not text:
            return Response({"error": "Missing 'text' field"}, status=status.HTTP_400_BAD_REQUEST)

        # Trigger Celery task
        task_result = process_text_task.delay(text)

        return Response({"message": "Task submitted", "task_id": task_result.id}, status=status.HTTP_202_ACCEPTED)