from google.appengine.ext.webapp.util import run_wsgi_app
from flask import Flask

coder_cooperative_app = Flask('ams-info-display')

@coder_cooperative_app.route('/')
def hello_world():
    return 'Hello World!'

run_wsgi_app(coder_cooperative_app)
