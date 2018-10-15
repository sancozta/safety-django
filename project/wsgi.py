import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
os.environ.setdefault('DISABLE_COLLECTSTATIC',  '1')

application = get_wsgi_application()
