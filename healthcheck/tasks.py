from celery import shared_task
import time

@shared_task
def health_check_task():
    return "Celery is running"

@shared_task
def process_text_task(text):
    """Simulate processing text asynchronously"""
    time.sleep(5)  # Simulate a delay (e.g., processing time)
    return f"Processed text new: {text.upper()}"