import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# decorator to create modified fixtures with parameters having the scope class
@pytest.fixture(params=['edge', 'firefox'],scope='class')
def init_driver(request):

    # request.param is helping us to overcome the redundancy of writing separate
    # code blocks for different browser
    # when the parameter is 'edge' we will install the driver of edge browser
    if request.param == 'edge':
        web_driver = webdriver.Edge(EdgeChromiumDriverManager().install())

    # when the parameter is 'firefox' we will install the driver of Firefox browser
    if request.param == 'firefox' :
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    request.cls.driver = web_driver

    yield
    web_driver.close()