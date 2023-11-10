from celery import shared_task
from .models import File

@shared_task
def processing(file_id):
    file = File.objects.get(id=file_id)
    file.processed = True
    file.save()