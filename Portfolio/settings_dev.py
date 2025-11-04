"""
Development settings for Portfolio project.
Use this file for local development only.
"""

from .settings import *

# Force debug mode
DEBUG = True

# Disable all HTTPS/SSL settings
SECURE_SSL_REDIRECT = False
SECURE_PROXY_SSL_HEADER = None
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False
SECURE_HSTS_SECONDS = 0

# Allow HTTP
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8000',
    'http://127.0.0.1:8000',
]

# Simplified allowed hosts
ALLOWED_HOSTS = ['localhost', '127.0.0.1']