from selenium import webdriver
#from fake_useragent import UserAgent
from time import sleep
import random

class ytbot():

    #links
    homepage_link = "https://www.youtube.com"
    login_link = "https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27"
    logout_link = "https://www.youtube.com/logout"

    #buttons and inputs (xpath)
    sign_up_with_google_button = '//*[@id="openid-buttons"]/button[1]'
    email_input = '//input[@type="email"]'
    email_next_button = '//*[@id="identifierNext"]'
    password_input = '//input[@type="password"]'
    password_next_button = '//*[@id="passwordNext"]'
    avatar_button = '//*[@id="avatar-btn"]'
    like_button = '//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[1]'
    dislike_button = '//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[2]'
    subscribe_button = '//*[@id="subscribe-button"]'
    unsubscribe_button = '//*[@id="confirm-button"]'

    def __init__(self):
        self.email = None
        self.password = None

        chrome_options = webdriver.ChromeOptions()
#        user_agent = UserAgent()
#        user_agent_value = user_agent.random
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--allow-running-insecure-content")
#        chrome_options.add_argument(f'user-agent={user_agent_value}')
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
        self.driver = webdriver.Chrome(options = chrome_options)

        return

    def login(self, email, password):
        self.email = email
        self.password = password

        self.driver.get(ytbot.login_link)
        sleep(random.uniform(1.5, 2))
        self.driver.find_element_by_xpath(ytbot.sign_up_with_google_button).click()
        sleep(random.uniform(1.5, 2))
        self.driver.find_element_by_xpath(ytbot.email_input).send_keys(email)
        sleep(random.uniform(1.5, 2))
        self.driver.find_element_by_xpath(ytbot.email_next_button).click()
        sleep(random.uniform(1.5, 2))
        self.driver.find_element_by_xpath(ytbot.password_input).send_keys(password)
        sleep(random.uniform(1.5, 2))
        self.driver.find_element_by_xpath(ytbot.password_next_button).click()
        sleep(random.uniform(1.5, 2))

        return

    def logout(self):
        self.driver.get(ytbot.logout_link)
        return

    def like_video(self, video_link):
        self.driver.get(video_link)
        sleep(random.uniform(1.5, 2))
        self.driver.find_element_by_xpath(ytbot.like_button).click()
        sleep(random.uniform(1.5, 2))
        return

    def dislike_video(self, video_link):
        self.driver.get(video_link)
        sleep(random.uniform(1.5, 2))
        self.driver.find_element_by_xpath(ytbot.like_button).click()
        sleep(random.uniform(1.5, 2))
        return

    def subscribe(self, channel_link):
        self.driver.get(channel_link)
        sleep(random.uniform(1.5, 2))
        self.driver.find_element_by_xpath(ytbot.subscribe_button).click()
        sleep(random.uniform(1.5, 2))
        return

    def unsubscribe(self, channel_link):
        self.driver.get(channel_link)
        sleep(random.uniform(1.5, 2))
        self.driver.find_element_by_xpath(ytbot.subscribe_button).click()
        sleep(random.uniform(1.5, 2))
        self.driver.find_element_by_xpath(ytbot.unsubscribe_button).click()
        sleep(random.uniform(1.5, 2))
        return
