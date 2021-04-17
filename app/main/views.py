from flask import render_template, request,redirect,url_for
from . import main
from ..requests import getnewsources
from ..models import Newssourcemodel,Newsarticlemodel


@main.route('/')
def home():

    sports = getnewsources('sports')
    entertainment = getnewsources('entertainment')
    science = getnewsources('science')
    business = getnewsources('business')
    health = getnewsources('health')
    technology = getnewsources('technology')

    title = 'NOTBBCNEWS'
    searchnews = request.args.get('news_querry')

    if searchnews:
        return redirect(url_for('.search',search_name = searchnews))
    else:
        return render_template('home.html', title = title, business = business, sports = sports, entertainment = entertainment, technology = technology,health = health, science = science)

    
@main.route
