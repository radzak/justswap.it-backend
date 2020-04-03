# -*- coding: utf-8 -*-

"""
Django settings for justswap project.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their config, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

from typing import Dict, List, Tuple, Union

from django.utils.translation import ugettext_lazy as ugt

from justswap.settings.components import BASE_DIR, config  # TODO: relative import?

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

SECRET_KEY = config("DJANGO_SECRET_KEY")

# Application definition:

INSTALLED_APPS: Tuple[str, ...] = (
    # Your apps go here:
    "justswap.accounts.apps.AccountsConfig",
    "justswap.main.apps.MainConfig",
    # Default django apps:
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # django-admin:
    "django.contrib.admin",
    "django.contrib.admindocs",
    # Security:
    "axes",
    # Health checks:
    # You may want to enable other checks as well,
    # see: https://github.com/KristianOellegaard/django-health-check
    "health_check",
    "health_check.db",
    "health_check.cache",
    "health_check.storage",
    # Third party apps
    "django_http_referrer_policy",
    "rest_framework",
    "djoser",
)

MIDDLEWARE: Tuple[str, ...] = (
    # Content Security Policy:
    "csp.middleware.CSPMiddleware",
    # Django:
    "django.middleware.security.SecurityMiddleware",
    "django_feature_policy.FeaturePolicyMiddleware",  # django-feature-policy
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Axes:
    "axes.middleware.AxesMiddleware",
    # Django HTTP Referrer Policy:
    "django_http_referrer_policy.middleware.ReferrerPolicyMiddleware",
)

ROOT_URLCONF = "justswap.urls"

WSGI_APPLICATION = "justswap.wsgi.application"

AUTH_USER_MODEL = "accounts.User"


LOGIN_REDIRECT_URL = "main:hello"


# Rest framework
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        # 'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        # 'rest_framework_social_oauth2.authentication.SocialAuthentication',
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 20,
}


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("POSTGRES_DB"),
        "USER": config("POSTGRES_USER"),
        "PASSWORD": config("POSTGRES_PASSWORD"),
        "HOST": config("DJANGO_DATABASE_HOST"),
        "PORT": config("DJANGO_DATABASE_PORT", cast=int),
        "CONN_MAX_AGE": config("CONN_MAX_AGE", cast=int, default=60),
        "OPTIONS": {"connect_timeout": 10},
    },
}


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

USE_I18N = True
USE_L10N = True

LANGUAGES = (
    ("en", ugt("English")),
    ("ru", ugt("Russian")),
)

LOCALE_PATHS = ("locale/",)

USE_TZ = True
TIME_ZONE = "UTC"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)


# Templates
# https://docs.djangoproject.com/en/2.2/ref/templates/api

TEMPLATES = [
    {
        "APP_DIRS": True,
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            # Contains plain text templates, like `robots.txt`:
            BASE_DIR.joinpath("justswap", "templates"),
        ],
        "OPTIONS": {
            "context_processors": [
                # Default template context processors:
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
            ],
        },
    }
]


# Media files
# Media root dir is commonly changed in production
# (see development.py and production.py).
# https://docs.djangoproject.com/en/2.2/topics/files/

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR.joinpath("media")


# Django authentication system
# https://docs.djangoproject.com/en/2.2/topics/auth/

AUTHENTICATION_BACKENDS = (
    "axes.backends.AxesBackend",
    "django.contrib.auth.backends.ModelBackend",
)

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.BCryptPasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
]


# Security
# https://docs.djangoproject.com/en/2.2/topics/security/

SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True

X_FRAME_OPTIONS = "DENY"

# https://github.com/DmytroLitvinov/django-http-referrer-policy
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy#Syntax
REFERRER_POLICY = "same-origin"

# https://github.com/adamchainz/django-feature-policy#setting
FEATURE_POLICY: Dict[str, Union[str, List[str]]] = {}  # noqa: WPS234


# Timeouts
EMAIL_TIMEOUT = 5
