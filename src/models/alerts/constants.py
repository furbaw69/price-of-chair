import os

__author__ = 'jslvtr'


URL = os.environ.get('MAILGUN_URL')
API_KEY = os.environ.get('MAILGUN_API')
FROM = os.environ.get('MAILGUN_FROM')
TO = os.environ.get('USER_EMAIL')
ALERT_TIMEOUT = 10
COLLECTION = "alerts"