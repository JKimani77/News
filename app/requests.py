import urllib.request, json
import json
from .models import Newssourcemodel,Newsarticlemodel



#getting api key
api_key = None

#getting base url
base_url = None
#getting articles url
articles_url = None

def configure_request(app):
    global api_key,base_url,articles_url
    api_key = app.config['NEWX_API_KEY']
    base_url = app.config['NEWX_API_BASE_URL']
    articles_url = app.config['NEWX_ARTICLES_BASE_URL']

def getnewsources(category):
    '''
    function to get response from api endpoint
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_newsdata = url.read()
        get_newsresponse = json.loads(get_newsdata)

        newsresults = None

        if get_newsresponse['sources']:
            news_ressultslist = get_newsresponse['sources']
            newsresults = process_newssources(news_ressultslist)

    return newsresults


def process_newssources(news_list):
    '''
    function to convert response from endpoint into object
    '''
    
    newsresults = []
    for i in news_list:
        id = i.get('id')
        name = i.get('name')
        description = i.get('description')
        category = i.get('category')
        url = i.get('url')
        language = i.get('language')
        country = i.get('country')

        if description:
            news_object = Newssourcemodel(id,name,description,url,category,country,language)
            newsresults.append(news_object)

    return newsresults


def getnewsarticles(news_id):
    '''
    function to get articles from api endpoint
    '''


    get_url = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'.format(news_id,api_key)

    with urllib.request.urlopen(get_url) as url:
        articles_info = url.read()
        articles_response = json.loads(articles_info)

        articlesresults = None

        if articles_response['articles']:
            search_articles = articles_response['articles']
            articlesresults = processarticles(search_articles)
    print(articlesresults)
    return articlesresults


def processarticles(my_articles):

    article_list = []

    for item in my_articles:
        author = item.get('author')
        title = item.get('title')
        description = item.get('description')
        url = item.get('url')
        urlToImage = item.get('urlToImage')

        if urlToImage:
            articlesource_obj = Newsarticlemodel(author, title, description, url, urlToImage)
            article_list.append(articlesource_obj)

    return article_list




