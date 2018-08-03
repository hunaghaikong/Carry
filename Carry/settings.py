"""
Django settings for Carry project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import djcelery
from mysite.HSD import get_config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(r7p=ea-$vntrx1cmct9nvt+q30%pltyi47!qu0wbxff*-wplt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#TEMPLATE_DEBUG=True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djcelery',
    'captcha',
    'mysite',
)


djcelery.setup_loader()     #加载djcelery
BROKER_URL = 'redis://127.0.0.1:6379/0'  #'pyamqp://guest@localhost//'    #配置broker
BROKER_POOL_LIMIT = 0
CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend'  #配置backend
CELERY_IMPORTS = ('mysite.tasks',)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'Carry.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

"""
# 开启缓存加载模版
TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)
"""

WSGI_APPLICATION = 'Carry.wsgi.application'
NEVER_REDIS_TIMEOUT=365*24*60*60 #此条可以省略

CACHES={
  'default':{
    'BACKEND':'django_redis.cache.RedisCache',
    'LOCATION':'127.0.0.1:6379',
    'OPTIONS':{'CLIENT_CLASS':'django_redis.client.DefaultClient',},
    },
}

# 关闭浏览器，session失效
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# 设置session，10个小时失效
SESSION_COOKIE_AGE = 60*60*10

# 优化session会话
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'a667',
        'USER': get_config('U','us'),
        'PASSWORD': get_config('U','ps'),
        'HOST': get_config('U','hs'),
        'PORT': 3306,
        'CONN_MAX_AGE': 1200, # 持久化数据库连接1200秒
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-Hans' #en-us

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#STATIC_ROOT=os.path.join(BASE_DIR,'static')
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR,'static')]
