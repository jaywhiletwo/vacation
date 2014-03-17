from project.settings.default import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS += ('192.168.1.7', )

INSTALLED_APPS += (
		'django_extensions',
		)

