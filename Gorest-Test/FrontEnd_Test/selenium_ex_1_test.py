from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
import pytest

class TestSet01(object):
    chrome_options = ChromeOptions()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    def setup_method(self):
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver',chrome_options=self.chrome_options)
        self.driver.get("https://gorest.co.in/rest-console.html")
    
    def teardown_method(self):
        self.driver.close()

    def test_basic(self):
        assert "Python" in self.driver.title
        elem = self.driver.find_element_by_class_name("btn btn-success")
        elem.click()
        returnElement = self.driver.find_element_by_class_name("alert ng-binding alert-success")
        assert "200 OK. Everything worked as expected." in returnElement.text