import unittest
from app.models import Newsarticlemodel
#author title description url UrlToImage

class Newssource(unittest.TestCase):

    def setUp(self):
        self.news = Newsarticlemodel('chadd', 'businessdaily', 'news blah blah blah ' ,'www.url.ulr', 'www.url.Image' )

    def test_instance(self):
        self.assertTrue(isinstance(self.news,Newsarticlemodel))