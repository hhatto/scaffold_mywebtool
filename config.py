import os.path

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8080
SERVER_MODULE = 'eventlet'

ROOT = os.path.abspath(os.path.dirname(__file__))
TEMPLATEM_ROOT = os.path.join(ROOT, 'templates')
STATIC_ROOT = os.path.join(ROOT, 'static')
