from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserAdditionalDetail


@receiver(post_save, sender=User)
def create_useradditionaldetail(sender, instance, created, **kwargs):
    if created:
        UserAdditionalDetail.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_useradditionaldetail(sender, instance, **kwargs):
    instance.useradditionaldetail.save()