from .base import *

DEBUG = True

INSTALLED_APPS += ('debug_toolbar',)

try:
	from .local import *
except ImportError:
	pass
