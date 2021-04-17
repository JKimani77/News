#id, name, description,url, category, language, country

class Newssourcemodel:

    def __init__(self,id,name,overview,news_image,person_posted,time_posted):
        self.id = id
        self.name = name
        self.overview = overview
        self.news_image = "https://image.tmdb.org/t/p/w500/" + news_image
        self.person_posted = person_posted
        self.time_posted = time_posted


class Newsarticlemodel:

    all_articles = []

    def __init__(self,article_id, title, article_image,article_description ):
        self.article_id = article_id
        self.title = title
        self.article_image = article_image
        self.article_description = article_description


    #classmethod
    #function for getting articles from arr
    #return

