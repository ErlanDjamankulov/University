from pathlib import Path
from dotenv import load_dotenv
import os


def str_to_bool(value):
    return value.lower() in ('true', '1', 'yes')


def get_env_variable(name, default=None, cast=str):
    value = os.getenv(name)
    if value is None:
        return default
    if cast is bool:
        return str_to_bool(value)
    if cast is not str:
        try:
            value = cast(value)
        except ValueError:
            raise ValueError(f"Cannot cast value of environment variable {name} to {cast}")
    return value


BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = get_env_variable("DEBUG", default=True, cast=bool)
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split()
DOCKER_STARTUP = os.getenv('DOCKER_STARTUP') == '1'

SERVER_IP = os.getenv("SERVER_IP", default="http://127.0.0.1:8000")
if SERVER_IP == "":
    SERVER_IP = "http://127.0.0.1:8000"

MY_APPS = [
    "apps.univer",
]

THIRD_PARTY_APPS = [
    "corsheaders",
    "rest_framework",
    "drf_yasg",

]
INSTALLED_APPS = ([
                      'modeltranslation',
                      'django.contrib.auth',
                      'django.contrib.contenttypes',
                      'django.contrib.sessions',
                      'django.contrib.messages',
                      'django.contrib.staticfiles',
                      "jazzmin",
                      'django.contrib.admin',
                      'allauth',
                      'allauth.account',
                      'allauth.socialaccount',
                      'allauth.socialaccount.providers.github',
                      'allauth.socialaccount.providers.google',
                      'dj_rest_auth',
                      'rest_framework.authtoken',
                      'django_filters',

                  ]
                  + MY_APPS
                  + THIRD_PARTY_APPS
                  )

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware",
    'django.middleware.locale.LocaleMiddleware',

]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
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

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

if DOCKER_STARTUP:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("POSTGRES_DB"),
            "USER": os.getenv("POSTGRES_USER"),
            "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
            "HOST": os.getenv("POSTGRES_HOST"),
            "PORT": os.getenv("POSTGRES_PORT"),
        }
    }

else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ru'
USE_L10N = True


LANGUAGES = (
    ('en','English'),
    ('ru', 'Russian'),
    ('ky', 'Kyrgyz')
)

LOCAL_PATHS = [
    BASE_DIR / 'locale/',
]
TIME_ZONE = "Asia/Bishkek"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOW_CREDENTIALS = get_env_variable("CORS_ALLOW_CREDENTIALS", cast=bool)
CORS_ALLOWED_ORIGINS = os.getenv("CORS_ALLOWED_ORIGINS").split()

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_HOST_ADMIN = os.getenv("EMAIL_ADMIN")

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": True,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-danger",
    "accent": "accent-primary",
    "navbar": "navbar-dark",
    "no_navbar_border": True,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": True,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": True,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": True,
    "sidebar_nav_flat_style": True,
    "theme": "superhero",
    "dark_mode_theme": "superhero",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    },
    "actions_sticky_top": True,
}

JAZZMIN_SETTINGS = {
    "site_title": "Univer",
    "site_header": "Univer",
    "welcome_sign": "Добро пожаловать в административную панель Univer",
    "changeform_format": "horizontal_tabs",
    "related_modal_active": True,
    "show_sidebar": True,
    "navigation_expanded": False,
    "searchbar_placeholder": "Поиск...",
    "searchbar_model_name": "Поиск по моделям...",
    "searchbar_model_field_name": "Поиск по полям...",
}

SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

SOCIALACCOUNT_PROVIDERS = {}


ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}
MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'
MODELTRANSLATION_LANGUAGES = ('ru','en','ky')