import os

import config
import jwt
from dotenv import load_dotenv
from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
from views import home_view

app = Flask(__name__, static_folder = 'static')
app.secret_key = config.APP_SECRET_KEY
csrf = CSRFProtect(app)

# Import View Blueprints
app.register_blueprint(home_view.bp)


config.init_app()


@app.context_processor
def context():
    """ Provide context variables to all routes and Jinja templates """
    return ({})


# Runs prior to every web request
@app.before_request
def init_req():
    """ Check application and user state before handling each request """
    pass

@app.route("/")
def home():
    return render_template('index.html')

# Run development web server with debugging
if __name__ == "__main__":
    load_dotenv(os.getcwd() + "/config.env")
    app.run(host="127.0.0.1", debug=True)#, ssl_context='adhoc')