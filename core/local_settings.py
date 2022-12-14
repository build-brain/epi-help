from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = '################'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': Path(BASE_DIR, 'db.sqlite3'),
    }
}

