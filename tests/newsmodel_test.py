import unittest
from app.models import Newssourcemodel
#id,name,description,language,url,category,country

class Newssource(unittest.TestCase):

    def setUp(self):
        self.news = Newssourcemodel(1,'bloomberg','news source that features latest news', 'www.news.news','en','business','usa')

    def test_instance(self):
        self.assertTrue(isinstance(self.news,Newssourcemodel))
