from flask import render_template, request,redirect,url_for
from . import main
from ..requests import getnewsources, getnewsarticles
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

    return render_template('home.html', title = title, business = business, sports = sports, entertainment = entertainment, technology = technology,health = health, science = science)

    
@main.route('/articles/<news_id>')
def articles(news_id):
    newsarticle = getnewsarticles(news_id)
    title = f'{news_id}'
    return render_template('articles.html', title = title, newsarticle = newsarticle)
