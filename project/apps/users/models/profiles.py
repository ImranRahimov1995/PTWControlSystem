from django.db import models

from utils.models.timestamp import TimeStamp


def get_avatar_place(instance, filename) -> str:
    return f'users/{instance.user}/avatar/{filename}'


class Profile(TimeStamp, models.Model):
    DUTY_CHOICES = (
        ("PA", "Some Ptw Maker"),
        ('AA', "Sahe Reisi"),
        ('OEE', "Operation Engineer"),
        ("OIM", "Reis"),
        ('Coordinator', "Coordinator"),
    )

    SEX_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    user = models.OneToOneField(
        'users.User',
        on_delete=models.CASCADE,
        related_name='profile',
    )
    photo = models.ImageField(upload_to=get_avatar_place, blank=True)

    sex = models.CharField(
        max_length=6, choices=SEX_CHOICES, blank=True, null=True
    )
    date_of_birth = models.DateField('Date of Birth ', blank=True, null=True)
    # need REGEX VALIDATION
    phone = models.CharField(max_length=12, blank=True, null=True)

    code = models.CharField(max_length=10, blank=True, null=True, unique=True)

    duty = models.CharField(max_length=100, choices=DUTY_CHOICES, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)

    def _get_code(self):
        if self.user.is_staff == True:
            self.code = self.pk
        else:
            count = Profile.objects.filter(duty=self.duty).count()
            if count == 0:
                count = 1
            self.code = f"{self.duty}-0{count}"

    def save(self, *args, **kwargs):
        self._get_code()
        return super().save(*args, **kwargs)
