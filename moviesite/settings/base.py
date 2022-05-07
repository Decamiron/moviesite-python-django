"""
Django settings for moviesite project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

SECRET_KEY = 'django-insecure-xt!&&z-o-m1i+t)zkr78#)m$r=1sw+waz97ld$re2np^_*3)6g'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    'search',

    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',

    'modelcluster',
    'taggit',

    'debug_toolbar',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users.apps.UsersConfig',
    'main.apps.MainConfig',
    'captcha'
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

ROOT_URLCONF = 'moviesite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_DIR, '../templates')],
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

WSGI_APPLICATION = 'moviesite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# JavaScript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/3.2/ref/contrib/staticfiles/#manifeststaticfilesstorage
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# Wagtail settings

WAGTAIL_SITE_NAME = "moviesite"

# Search
# https://docs.wagtail.org/en/stable/topics/search/backends.html
WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.search.backends.database',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'moviesite_cache'),
    }
}
# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash

# STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# Debug toolbar
INTERNAL_IPS = ['127.0.0.1', ]


BASE_URL = 'http://example.com'
AUTH_USER_MODEL = 'users.MyUser'
CAPTCHA_IMAGE_SIZE = (200, 100)
CAPTCHA_FONT_SIZE = 44
DEFAULT_IMAGE = 'data:image/jpeg;base64,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'