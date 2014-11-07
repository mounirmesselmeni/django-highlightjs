import django.conf.global_settings as DEFAULT_SETTINGS


SECRET_KEY = 'highlightjsisawesome'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

INSTALLED_APPS = (
    'highlightjs',
)

MIDDLEWARE_CLASSES = DEFAULT_SETTINGS.MIDDLEWARE_CLASSES
