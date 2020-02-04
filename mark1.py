from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome()

    def login(self):
        bot = self.bot
        bot.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        time.sleep(8)
        email = bot.find_element_by_class_name('_2hvTZ')
        password = bot.find_element_by_name('password')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(5)

    def like_post(self, hashtag):
        bot = self.bot
        bot.get('https://www.instagram.com/explore/tags/'+hashtag)
        time.sleep(3)
        for i in range(1,3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(4)
        posts = bot.find_elements_by_class_name('v1Nh3')
        links = []
        for post in posts:
            links.append(post.find_element_by_tag_name('a').get_attribute('href'))
        for link in links:
            bot.get(link)
            try:
                bot.find_element_by_class_name('_8-yf5').click() #class name may change, find the apt class name by inspecting instagram website
            except Exception as e:
                time.sleep(5)
        
ap = InstagramBot("USERNAME", "PASSWORD")
ap.login()
ap.like_post('fitness') #whatever tags posts you want to like
