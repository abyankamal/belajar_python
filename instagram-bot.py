from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


TARGET_ACCOUNT_URL = "https://www.instagram.com/buzzfeedtasty/"
SIMILAR_ACCOUNT = "buzzfeedtasty" # Change this to an account of your choice
USERNAME = "kamalmuhammad414"
PASSWORD = "rahasiaumum"


class InstaFollower:

    def __init__(self):
        # Keep browser open so you can manually log out
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    # Avoid bot-like behaviour and try not to run your script too often.
    def login(self):
        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)
        time.sleep(4.2)

        # Check if the cookie warning is present on the page
        decline_cookies_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]"
        cookie_warning = self.driver.find_elements(By.XPATH, decline_cookies_xpath)
        if cookie_warning:
            # Dismiss the cookie warning by clicking an element or button
            cookie_warning[0].click()

        username = self.driver.find_element(by=By.NAME, value="username")
        password = self.driver.find_element(by=By.NAME, value="password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2.1)
        password.send_keys(Keys.ENTER)

        time.sleep(4.3)
        # Click "Not now" and ignore Save-login info prompt
        save_login_prompt = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        if save_login_prompt:
            save_login_prompt.click()

        time.sleep(3.7)
        # Click "not now" on notifications prompt
        notifications_prompt = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Not Now')]")
        if notifications_prompt:
            notifications_prompt.click()

    def find_followers(self):
        self.driver.get(url=TARGET_ACCOUNT_URL)
        time.sleep(5)
        followers_list = self.driver.find_element(By.XPATH, value='//html/body/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
        followers_list.click()
        time.sleep(3)
        dialog = self.driver.find_element(By.XPATH, value='/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        for i in range (10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", dialog)
            time.sleep(2)

    def follow(self):
        dialog = self.driver.find_element(By.XPATH, value='/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        follow_buttons = dialog.find_elements(By.TAG_NAME, value='button')
        for element in follow_buttons:
            try:
                element.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, value='//button[contains(text(), "Cancel")]')
                cancel_button.click()
                time.sleep(1)


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
