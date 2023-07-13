from flask import Blueprint, flash, redirect, render_template, request
import config

from control import home

bp = Blueprint('home', __name__)

@bp.route("/home/")
def user_home():
    data = home.get_dashboard_data()
    return render_template('home.html', data=data)