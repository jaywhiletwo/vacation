from project.settings.default import *
# LIVE SETTINGS

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Make this unique, and don't share it with anybody.
import os
SECRET_KEY = os.environ['SECRET_KEY']

