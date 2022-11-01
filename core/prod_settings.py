from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = '####################'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '176.96.243.121']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'epi-help',
        'USER': 'epi',
        'PASSWORD': 'epi123',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# STATIC_DIR = Path(BASE_DIR, 'static')
# STATICFILES_DIR = [STATIC_DIR]
# STATIC_ROOT = Path(BASE_DIR, 'static')
