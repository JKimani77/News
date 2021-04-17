#id, name, description,url, category, language, country

class Newssourcemodel:

    def __init__(self,id,name,description,language,url,category,country):
        self.id = id
        self.name = name
        self.description = description
        self.language = language
        self.url = url
        self.category = category
        self.country = country


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

