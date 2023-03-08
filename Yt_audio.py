from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import re
import time
from urllib.parse import urlparse, parse_qs

class music():
    def __init__(self):
        service = Service('C:\Drivers\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)

    def play(self, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
        video = self.driver.find_element(By.XPATH, '//*[@id="video-title"]/yt-formatted-string')
        video.click()
        time.sleep(5)  # add a delay here to give the video time to load
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(300)
        self.driver.close()

# assist=music()
# assist.play("Love me Like you do")
