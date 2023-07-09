from crayons import red, yellow, green
from time import sleep
import uwsgi

APP_TAG="FLASK_FWK"
APP_SECRET_KEY=b"uykiy&66&^8796"
wid = uwsgi.worker_id()

def init_app():
    print(green("Initialising Application..."))
    
    print(green("Application Initialised"))