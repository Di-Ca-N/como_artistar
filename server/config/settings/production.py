from .base import *

DEBUG = False
SECRET_KEY = "alguma-secret-key-muito-legal"
ALLOWED_HOSTS = ["dican.pythonanywhere.com"]

try:
    from .local import *
except ImportError:
    pass
