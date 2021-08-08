import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# @pytest.fixture(params=['edge', 'firefox'],scope='class')
# def init_driver(request):
#     if request.param == 'edge':
#         web_driver = webdriver.Edge(EdgeChromiumDriverManager().install())
#
#     if request.param == 'firefox' :
#         web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#
#     request.cls.driver = web_driver
#
#     yield
#     web_driver.close()

@pytest.mark.usefixtures('init_driver')
class BaseTest :
    pass

class Test_google(BaseTest):

    def test_google_title(self):
        self.driver.get('http://www.google.com')
        assert self.driver.title == "Google"