from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class infow():
    def __init__(self):
        # self.driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver.exe')
        service = Service('C:\Drivers\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)

    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org")
        # search=self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        search = self.driver.find_element(By.XPATH, '//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/fieldset/button')
        enter.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(30)
        self.driver.close()


# assist = infow()
# assist.get_info("google")
