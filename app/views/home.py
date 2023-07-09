from flask import Blueprint, flash, redirect, render_template, request
import config

bp = Blueprint('home', __name__)

@bp.route("/")
def home():
    return render_template('index.html')

@bp.route("/home/")
def user_home():
    return render_template('index.html')