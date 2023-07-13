# flask-base
A bare-bones docker container template including python 3.9, Flask, uWSGI & NGINX.

- Folder structure to encourage the separation of code as per MVC practices.
- CSRF protection enabled by default to protect your POST data


# Getting Started
'git clone https://github.com/ojbulman/flask-base.git'
'python -m venv env'
Linux: 'source ./env/bin/activate'
Windows: './env/Scripts/activate'
'python -m pip install --upgrade pip'
'pip install -r requirements.txt'
'docker build -t flask-app:0.1.0 .'
'docker run -d -p 7000:80 --env-file ./config/config.env --name="FlaskApp" flask-app:0.1.0'

# Important notes
If adding your secrets / passwords / API keys to the /config/config.env file, ensure that this is excluded from any git commits. The .gitignore file includes a commented out exclusion rule at the top which can should be uncommented.

## Extensions
Extension Modules & Blueprints can be found at [ojbulman/flask-utils]('https://github.com/ojbulman/flask-utils')
- Flask Authentication - Role based authentication
- uWsgi Queueing - Thread Safe Background task queueing

# Files & Folders
/config
    config.env  - Store any required secrets in here. These will be created as environment variables when running the container
    flask-site-nginx.conf   - URL routing configuration used by Nginx. This may be edited as required.
    nginx.conf  - Core Nginx configuration
    uwsgi.ini   - uWsgi configuration options with recommended default settings. Additionally, threading is enabled and uWsgi cacheing is disabled. This may be amended as required for your project.
    supervisord.conf    - OS Supervisor configuration for runnung Nginx and uWsgi.
/app    - Project root.
    main.py - Your application entry point. Initialise application and import view blueprints here.
    config.py   - Intended for managing App configuration and global configuration options
    /templates  - HTML Templates
    /static     - Static files such as images, css and javascript files
    /imports    - Imported utility modules
    /views      - View Blueprints containing app route functions
    /models     - Modal centric modules for direct interacting with your stored data
    /control    - Process functions fetching data from model functions or API's, and returning data to View functions
