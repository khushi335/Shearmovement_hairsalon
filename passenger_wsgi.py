import sys
import os

# Project path
project_home = '/home/hightech/shearmovement.quantumcoresoftware.com/salon'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Activate virtualenv
activate_env = '/home/hightech/virtualenv/shearmovement.quantumcoresoftware.com/salon/3.10/bin/activate_this.py'
with open(activate_env) as f:
    exec(f.read(), dict(__file__=activate_env))

# Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'salon.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()