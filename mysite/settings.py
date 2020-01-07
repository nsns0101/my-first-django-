"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0wi&293j(ae)w8h!k456q0#ip23m5^c3vio23_cicav55$-s$a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True    #True로 주면 웹 서버의 정보가 브라우저에 노출되므로 배포시에는 반드시 False를 줄 것
                 #DEBUG를 못하도록 설정.

ALLOWED_HOSTS = ['localhost', '127.0.0.1']   #허용되는 주소


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',         #홈페이지
    'accounts',     #로그인, 회원가입
]   #앱 추가

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR,'templates'],  #앱밖의 templates에 들어갈 수 있게 해줌
        'APP_DIRS': True,       #앱안의 templates를 들어갈 수 있게 해줌
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   #쓸 DB
        'NAME': 'mysite',                       #DB명
        'USER' : 'root',                        #SQL ID
        'PASSWORD' : 'node',                    #SQL PASSWORD
        'HOST' : 'localhost',                   #HOST
        'PORT' : '',                            #PORT(생략시 localhost:8000)
        'CHARSET' : 'utf8mb4',                     
        'COLLATION' : 'utf8mb4_unicode_ci',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'     #언어설정

TIME_ZONE = 'Asia/Seoul'    #시간 설정

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/' #웹페이지에서 사용할 정적파일의 최상위 url경로

LOGIN_REDIRECT_URL = '/'


AUTH_USER_MODEL = 'accounts.models'     #User모델을 커스터마이징할 경우 써야함

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)