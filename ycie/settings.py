"""
Django settings for ycie project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import environ

env = environ.Env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.get_value("SECRET_KEY", default=os.environ.get("SECRET_KEY"))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_jinja',

    'account',
    'application',
    'house',
    'statistic'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ycie.urls'


TEMPLATES = [
    {
        "BACKEND": "django_jinja.backend.Jinja2",
        "APP_DIRS": True,
        "OPTIONS": {
            'autoescape': True,
            "match_extension": ".html",
            "app_dirname": os.path.join(BASE_DIR, 'templates', 'jinja'),
            "translation_engine": "django.utils.translation",
            "extensions": [
                "jinja2.ext.do",
                "jinja2.ext.loopcontrols",
                "jinja2.ext.with_",
                "jinja2.ext.i18n",
                "jinja2.ext.autoescape",
                "django_jinja.builtins.extensions.CsrfExtension",
                "django_jinja.builtins.extensions.CacheExtension",
                "django_jinja.builtins.extensions.TimezoneExtension",
                "django_jinja.builtins.extensions.UrlsExtension",
                "django_jinja.builtins.extensions.StaticFilesExtension",
                "django_jinja.builtins.extensions.DjangoFiltersExtension",
            ],
            "bytecode_cache": {
                "name": "default",
                "backend": "django_jinja.cache.BytecodeCache",
                "enabled": False,
            },
        }
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'ycie.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        "ENGINE": 'django.db.backends.postgresql_psycopg2',
        "NAME": env.get_value("BD_NAME", default=os.environ.get("BD_NAME")),
        "USER": env.get_value("DB_USER", default=os.environ.get("DB_USER")),
        "PASSWORD": env.get_value("DB_PASSWORD", default=os.environ.get("DB_PASSWORD")),
        "HOST": env.get_value("DB_HOST", default=os.environ.get("DB_HOST")),
        "PORT": env.get_value("DB_PORT", default=os.environ.get("DB_PORT")),
    }
}

CACHES = {
    "default": {
        "BACKEND": env.get_value("CACHE_BACKEND", default=os.environ.get("CACHE_BACKEND")),
        "LOCATION": env.get_value("CACHE_LOCATION", default=os.environ.get("CACHE_LOCATION")),
        "OPTIONS": {
            "CLIENT_CLASS": env.get_value("CACHE_CLIENT_CLASS", default=os.environ.get("CACHE_CLIENT_CLASS")),
        }
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"

AUTH_USER_MODEL = "account.User"


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATIC_URL_PATH = 'static'
MEDIA_URL_PATH = 'media'
STATICFILES_LOCATION = STATIC_URL_PATH
MEDIA_LOCATION = MEDIA_URL_PATH

STATIC_URL = env.get_value("STATIC_URL", default=os.environ.get("STATIC_URL"))
if STATIC_URL:
    STATIC_URL = "".join(['/', STATIC_URL_PATH, '/'])

MEDIA_URL = env.get_value("MEDIA_URL", default=os.environ.get("MEDIA_URL"))
if MEDIA_URL:
    MEDIA_URL = "".join(['/', MEDIA_URL_PATH, '/'])

