from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from RMS.models.RestaurantWorkerRole import RestaurantWorkerRole
from RMS.models.RestaurantWorker import RestaurantWorker


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_worker_for_user(sender, instance=None, created=False, **kwargs):
    if created:
        user_worker = RestaurantWorker(user=instance)
        if instance.is_superuser:
            user_worker.roles = [RestaurantWorkerRole.SYSTEM]
        user_worker.save()
