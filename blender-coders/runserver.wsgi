import sys

activate_this = '/data/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
from flup.server.fcgi import WSGIServer

sys.path.append('/data/git/blender-coders/blender-coders/')
from app import app as application

if __name__ == '__main__':
    WSGIServer(application).run()
