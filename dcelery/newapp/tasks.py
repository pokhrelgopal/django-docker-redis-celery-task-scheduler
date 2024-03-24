from datetime import timedelta
from django.utils import timezone
from celery import shared_task
from .models import Todo
import logging

logger = logging.getLogger(__name__)


@shared_task
def delete_completed_todo():
    try:
        todo = Todo.objects.filter(
            completed=True, completed_at__lte=timezone.now() - timedelta(seconds=10)
        )
        todo.delete()
    except Exception as e:
        logger.error(f"Error occurred while deleting completed todo: {e}")
