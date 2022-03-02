import os

from .base import *

DEBUG = False

SECRET_KEY = os.getenv(
    'DJANGO_SECRET_KEY',
    'django-insecure-d)-9&oks3j52p0m0-tn#i)zmc(z$g0o24ls9^gxnfujdik_+*#'
)

ALLOWED_HOSTS = [
    os.getenv('PUBLIC_IP', '*'),
    os.getenv('DOMAIN_NAME', '*'),
    os.getenv('WWW_DOMAIN_NAME', '*'),
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_APP', 'app_db'),
        'USER': os.getenv('DB_USER', 'admin'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'devpass'),
        'HOST': os.getenv("DB_HOST", "postgresdb"),
        'PORT': os.getenv("DB_PORT", "5432"),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'smtp_sender@mail.ru'


EMAIL_HOST = 'smtp.mail.ru'
EMAIL_PORT = 2525
EMAIL_HOST_USER = 'smtp_sender@mail.ru'
EMAIL_HOST_PASSWORD = os.environ.get('MYPASS', 'v0hRbpS3bfB3PRhx2Zvi')
EMAIL_USE_TLS = True
