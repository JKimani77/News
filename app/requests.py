import urllib.request, json
from .models import Newssourcemodel



#getting api key
api_key = None

#getting base url
base_url = None
#getting articles url
articles_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWX_API_KEY']
    base_url = app.config['NEWX_API_BASE_URL']
    articles_url = app.config['NEWX_ARTICLES_BASE_URL']

def getnewsources(category):

    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_newsdata = url.read()
        get_newsresponse = json.loads(get_newsdata)

        newsresults = None

        if get_newsresponse['results']:
            news_ressultslist = get_newsresponse['results']
            newsresults = process_newssources(news_ressultslist)

    return newsresults


def process_newssources(news_list):
    #funct that process news result
    #and transform to list of obj
    #news_list is a list of dictionaries containing news detasils
    #returns a list of news objects
    
    newsresults = []
    for i in news_list:
        id = i.get('id')
        title = i.get(title)
        overview = i.get('overview')
        news_image = i.get('news_image')
        person_posted = i.get('person_posted')
        time_posted = i.get('time_posted')

        if news_image:
            news_object = Newssourcemodel(id,title,overview,news_image,person_posted,time_posted)
            newsresults.append(news_object)

    return newsresults

