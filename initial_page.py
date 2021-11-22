from time import sleep
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

import sys

'''INPUT if page in english then "en = True" elif page in french "en = False" (for now, only en and fr)'''
en = True
not_now = "Not Now" if en else "Plus tard"
accept_all = "Accept All" if en else "Accepter tout"
'''
class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        username_input = self.browser.find_element_by_css_selector("input[name='username']")
        password_input = self.browser.find_element_by_css_selector("input[name='password']")
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button = self.browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        sleep(2)

class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')

    def go_to_login_page(self):
        # self.browser.find_element_by_xpath("//*[text()='Log in']").click()
        sleep(2)
        return LoginPage(self.browser)

'''

class Browser:
    def __init__(self, browser):
        self.browser = browser

    def surf(self, site=""):
        if not site:
            self.browser.get("https://www.instagram.com/")
            return
        self.browser.get(input())

    def login(self, username, password):
        username_input = self.browser.find_element_by_css_selector("input[name='username']")
        password_input = self.browser.find_element_by_css_selector("input[name='password']")
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button = self.browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        sleep(2)

    def plus_tard(self):
        sleep(2)
        later_button = self.browser.find_element_by_xpath("//*[text()='" + not_now + "']")
        later_button.click()

    def accepter_tout(self):
        sleep(2)
        accepter_tout = self.browser.find_element_by_xpath("//*[text()='" + accept_all + "']")
        accepter_tout.click()


def browse(chrome_options=""):
    if chrome_options:
        browser = webdriver.Chrome("/home/kali/Downloads/chromedriver")
        return browser
    chrome_options=Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    browser = webdriver.Chrome("/home/kali/Downloads/chromedriver", options=chrome_options)
    return browser


def main(browser0):
    browser0.implicitly_wait(5)

    browser = Browser(browser0)
    browser.surf()
    browser.accepter_tout()
    browser.login("aymane.dassouli@gmail.com", "Aymane..")
    browser.plus_tard()
    browser.plus_tard()
    sleep(10)

if __name__ == '__main__':
    with browse() as browser0:
        main(browser0)


'''
def test_login_page(browser):
    home_page = HomePage(browser)
    login_page = home_page.go_to_login_page()
    login_page.login("aymane.dassouli@gmail.com", "Aymane..")

    errors = browser.find_element_by_css_selector('#error_message')
    assert len(errors) == 0
'''


