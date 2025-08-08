import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', 'your-default-secret-key')

DEBUG = False  # حتما در پروداکشن False باشه

# ALLOWED_HOSTS = ['your-render-url.onrender.com', 'localhost', '127.0.0.1']

INSTALLED_APPS = [
    # اپلیکیشن‌های خودت و اپ‌های پیشفرض جنگو
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myappp'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # این برای سرو کردن فایل استاتیک هست
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # مسیر قالب‌ها
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

WSGI_APPLICATION = 'Modernized-Tea-Station.wsgi.application'

# دیتابیس (اگر از PostgreSQL استفاده می‌کنی)

# فایل‌های استاتیک
STATIC_URL = '/static/'

# این دایرکتوری جایی است که collectstatic فایل‌ها را آنجا جمع می‌کند
STATIC_ROOT = BASE_DIR / 'staticfiles'

# اگر فولدر استاتیک اضافه داری (مثل پوشه static در ریشه پروژه)
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # اگر چنین فولدری داری؛ اگر نداری میتونی حذفش کنی
]

# استفاده از whitenoise برای سرو کردن استاتیک‌ها در پروداکشن
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# تنظیمات مربوط به رسانه (اگر داری)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# سایر تنظیمات مثل زبان، timezone و ...

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
