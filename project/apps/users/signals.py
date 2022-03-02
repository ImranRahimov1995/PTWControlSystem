from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.users.models import User, Profile


@receiver(post_save,sender=User)
def profile_create(sender, **kwargs):
    print(kwargs)
    Profile.objects.create(user=kwargs['instance'])
