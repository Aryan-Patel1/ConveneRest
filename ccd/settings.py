"""
Django settings for ccd project.

Generated by 'django-admin startproject' using Django 1.9.12.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see     
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_ws4dz#pxyx8*5!@bcbme5%t@u-wjh+iezh-31c7)21-5qr39w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

HOST_URL = "http://127.0.0.1:8091/"

FRONT_URL = "https://meal.mahiti.org"

LDAP_URL = "ldap://192.168.1.5"
# Application definition

FY_YEAR = '2018'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'django_extensions',
    'rest_framework',
    'rest_framework_swagger',
    'rest_framework.authtoken',
    'masterdata.apps.MasterdataConfig',
    'userroles.apps.UserrolesConfig',
    'corsheaders',
    'beneficiary.apps.BeneficiaryConfig',
    'facilities.apps.FacilitiesConfig',
    'partner.apps.PartnerConfig',
    'service.apps.ServiceConfig',
    'survey.apps.SurveyConfig',
    'dynamic_listing.apps.DynamicListingConfig',
    'meeting.apps.MeetingConfig',
    'workflow.apps.WorkflowConfig',
    'reports.apps.ReportsConfig',
    'silk',
    'report_views.apps.ReportViewsConfig',
#    'MutantApp.apps.MutantappConfig',
#    'mutant',
#    'mutant.contrib.boolean',
#    'mutant.contrib.temporal',
#    'mutant.contrib.file',
#    'mutant.contrib.numeric',
#    'mutant.contrib.text',
#    'mutant.contrib.web',
#    'mutant.contrib.related',
]

MIDDLEWARE_CLASSES = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.middleware.common.CommonMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True

#CORS_ORIGIN_WHITELIST = ('hufpartners.akasmika.net')

CORS_ALLOW_CREDENTIALS = False

CORS_ALLOW_HEADERS = ( 'x-requested-with', 'content-type', 'accept', 'origin', 'authorization', 'x-csrftoken' )

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)

website_data = {1: {'webiste': 'http://meal.mahiti.org/',
                   'donar': 'http://meal.mahiti.org/listing/#/donor/Listing',
                   'funding': 'http://meal.mahiti.org/listing/#/DPF/ManageFunding/'},
               2: {'webiste': 'http://cryui.mahiti.org/',
                   'donar': 'http://cryui.mahiti.org/listing/#/donor/Listing',
                   'funding': 'http://cryui.mahiti.org/listing/#/DPF/ManageFunding/'}}

#web_dict = website_data.get(2)
web_dict = {}

REST_FRAMEWORK = {
   'DEFAULT_AUTHENTICATION_CLASSES': (
       'userroles.authentication.ExpiringTokenAuthentication',
   ),
#    'DEFAULT_PERMISSION_CLASSES': (
#        'rest_framework.permissions.IsAuthenticated',
#    ),
   'DEFAULT_RENDERER_CLASSES': (
       'rest_framework.renderers.JSONRenderer',
       'rest_framework.renderers.BrowsableAPIRenderer',
   ),
   'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
   'PAGE_SIZE': 10,
   'DPF_PAGE_SIZE': 10,
   'MASTERDATA_LOCATION': 50,
}

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'api_key': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    },
}


ROOT_URLCONF = 'ccd.urls'

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

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'ghostsarereal'
EMAIL_HOST_PASSWORD = 'ghost@21'
EMAIL_PORT = 587

WSGI_APPLICATION = 'ccd.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cry_prod_new',
        'USER': 'cry_live',#cryconvene,cry_new,demo_new,cry_live
        'PASSWORD': 'cry_live',
        'HOST': 'localhost',
        'PORT': 5432,
        'AUTOCOMMIT': True,
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

"""
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
]"""


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (BASE_DIR + '/static/',)
