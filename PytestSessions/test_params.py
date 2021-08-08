import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures('init_driver')
class BaseCase():
    pass


class TestFacebook(BaseCase):


    @pytest.mark.parametrize("username , password" ,[
        ("random@gmail.com", "1234567"),
        ("random@yahoo.com", "abcde"),
        ("random@outlook.com", "123asdghj")
    ])
    def test_fb(self, username, password):
        """
        This method navigates to facebook and try to log into facebooj
        :param username:
        :param password:
        :return:
        """
        self.driver.get('https://www.facebook.com/')
        name = self.driver.find_element(By.XPATH, "//input[@id='email']")
        pass_word = self.driver.find_element(By.XPATH, "//input[@id='pass']")
        name.send_keys(username)
        pass_word.send_keys(password)
