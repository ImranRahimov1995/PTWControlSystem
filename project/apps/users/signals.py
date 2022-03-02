from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.users.models import User, Profile


@receiver(post_save, sender=User)
def profile_create(sender, **kwargs):
    created = kwargs['created']
    user = kwargs.get('instance', None)
    print(created)
    if user:

        if user.is_staff:
            return False
        if not created:
            return False
        else:
            print('popal')
            Profile.objects.create(user=user)
