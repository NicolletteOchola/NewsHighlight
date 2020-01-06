import urllib.request, json
from .models import Sources, Articles
from datetime import datetime

api_key = None
sources_url = None
articles_url = None
topheadlines_url = None
everything_url = None
everything_search_url = None

def configure_request(app):
  global api_key, sources_url, articles_url, topheadlines_url, everything_url, everything_search_url
  api_key = app.config['NEWS_API_KEY']
  sources_url = app.config['SOURCES_BASE_URL']
  articles_url = app.config['EVERYTHING_SOURCE_BASE_URL']
  topheadlines_url = app.config['TOP_HEADLINES_BASE_URL']
  everything_url = app.config['EVERYTHING_BASE_URL']
  everything_search_url = app.config['EVERYTHING_SEARCH_URL']