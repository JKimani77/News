from  flask import render_template
from . import main

@main.app_errorhandler(404)
def errorforrowfor(error):
    return render_template('foh_oh_foh.html'),404