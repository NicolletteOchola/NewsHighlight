from flask import render_template,redirect,url_for,request
from . import main
from ..models import Sources
from ..request import get_sources, get_articles, topheadlines, everything, search_everything

@main.route('/')
def index():
  '''
  Function for the view root oage that returns the index page and it's data
  '''
  cat_general = get_sources('general')
    cat_business = get_sources('business')
    cat_entertainment = get_sources('entertainment')
    cat_sports = get_sources('sports')
    cat_tech = get_sources('technology')
    cat_science = get_sources('science')
    cat_health = get_sources('health')

    title = 'Home | Reliable News'

    return render_template('index.html',title=title, general=cat_general, business = cat_business, entertainment = cat_entertainment, sports = cat_sports, tech = cat_tech, science = cat_science, health = cat_health)