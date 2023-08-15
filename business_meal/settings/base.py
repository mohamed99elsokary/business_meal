"""
Django settings for business_meal project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from datetime import timedelta
from os.path import join, normpath
from pathlib import Path

from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY", default=False, cast=str)
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = ["*"]

AUTH_USER_MODEL = "userapp.User"
AUTHENTICATION_BACKENDS = ["django.contrib.auth.backends.AllowAllUsersModelBackend"]
# Application definition


DJANGO_APPS = [
    "unfold",
    "unfold.contrib.filters",
    "unfold.contrib.forms",
    "unfold.contrib.import_export",
    "modeltranslation",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
]
THIRD_PARTY_APPS = [
    "allauth",
    "allauth.account",
    "dj_rest_auth.registration",
    # rest framework
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    "import_export",
    "django_filters",
    # all auth
    "allauth.socialaccount",
    "allauth.socialaccount.providers.facebook",
    "dj_rest_auth",
    "drf_yasg",
]
# local apps
LOCAL_APPS = [
    'business_meal.order_app',
    'business_meal.hotel_app',
    'business_meal.openbuffet_app',
    "business_meal.resturant_app",
    "business_meal.userapp",
    "business_meal.addonsapp",
    "business_meal.services",
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
SITE_ID = 1


MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "business_meal.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


WSGI_APPLICATION = "business_meal.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# sqlite3 database

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# postgresql
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": config("POSTGRES_DB", cast=str),
#         "USER": config("POSTGRES_USER", cast=str),
#         "PASSWORD": config("POSTGRES_PASSWORD", cast=str),
#         "HOST": config("POSTGRES_HOST", cast=str),
#         "PORT": config("POSTGRES_PORT", cast=str),
#         "ATOMIC_REQUESTS": True,
#     }
# }
# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en"

TIME_ZONE = "Africa/Cairo"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

gettext = lambda s: s  # noqa
LANGUAGES = (("en", gettext("English")), ("ar", gettext("Arabic")))
MODELTRANSLATION_DEFAULT_LANGUAGE = "en"

LOCALE_PATHS = (normpath(join(BASE_DIR, "locale")),)


STATIC_DIRECTORY = "/static/"
MEDIA_DIRECTORY = "/media/"

AUTH_PASSWORD_VALIDATORS = []
AWS_QUERYSTRING_AUTH = False


""" CORS ORIGIN """
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True


""" REST FRAMEWORK """
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PAGINATION_CLASS": "business_meal.services.paginator.CustomPagination",
    "PAGE_SIZE": 5,
    "DEFAULT_FILTER_BACKENDS": (
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
    ),
}

""" JWT Settings"""

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
    "AUTH_HEADER_TYPES": ("Token",),
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
}

"""Import Export"""
IMPORT_EXPORT_USE_TRANSACTIONS = True


""" SWAGGER_SETTINGS """
SWAGGER_SETTINGS = {
    "DEFAULT_AUTO_SCHEMA_CLASS": "business_meal.swagger.CustomSwaggerAutoSchema",
    "LOGIN_URL": "/admin/login/",
    "LOGOUT_URL": "/admin/logout/",
    "PERSIST_AUTH": True,
    "DEEP_LINKING": True,
    "DOC_EXPANSION": "none",
    "SECURITY_DEFINITIONS": {
        "JWT": {"type": "apiKey", "name": "Authorization", "in": "header"},
    },
}


""" All Auth Settings"""
# https://django-allauth.readthedocs.io/en/latest/configuration.html
SOCIALACCOUNT_PROVIDERS = {}
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
""" Rest Auth settings """
REST_USE_JWT = True
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_UNIQUE_EMAIL = True
