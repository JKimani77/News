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

    def __init__self, author, title, description, url, urlToImage ):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage


    #classmethod
    #function for getting articles from arr
    #return

