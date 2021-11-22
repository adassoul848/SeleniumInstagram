import selenium.common.exceptions
from initial_page import Browser, browse
import time
from bs4 import BeautifulSoup

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from random import random

def random_wait(max=3):
    return (random()-1)*3 + max

class Interact(Browser):

    '''click on the firt picture in the page'''
    def firstpic_click(self):
        time.sleep(random_wait())
        first = self.browser.find_element_by_class_name("kIKUG")
        first.click()

    '''likes curent picture'''
    def like_pic(self):
        time.sleep(random_wait())
        like = self.browser.find_element_by_class_name("fr66n")
        soup = BeautifulSoup(like.get_attribute('innerHTML'),'html.parser')

        if (soup.find('svg')['aria-label'] == 'Like'):
            like.click()

        time.sleep(random_wait())

    ''' returns and clicks on next picture if any'''
    def next_picture(self):
        time.sleep(random_wait())
        try:
    #       nex = browser.find_element_by_xpath('//svg[@aria-label="Next"]')
            next = self.browser.find_elements_by_class_name("wpO6b  ")
            soups = [BeautifulSoup(nextt.get_attribute('innerHTML'),'html.parser') for nextt in next]
            for i in range(len(soups)):
                #print(soups[i])
                if (soups[i].find('svg')['aria-label'] == 'Next'):
                    return next[i]
            #nex = self.browser.find_element_by_xpath('//button[@class="wpO6b  "]')
            #time.sleep(1)
            #return nex
        except selenium.common.exceptions.NoSuchElementException:
            return 0

    ''' liking all the next pictures if any'''
    def continue_liking(self):
        while(True):
            next_el = self.next_picture()
            if next_el != False:
                self.like_pic()
                time.sleep(random_wait())
                next_el.click()
                time.sleep(random_wait())
            else:
                print("not found")
                break

    def word_search(self, search=1):
        # word = input("what?")
        word = "travel"
        #search is the method of search

        #looking for word in search box
        if search == 0:
            search_box = self.browser.find_element_by_xpath("//input[@aria-label='Search Input']")
            search_box.send_keys("#"+word)
            time.sleep(random_wait())
            #search_box.send_keys(Keys.RETURN)
            #search_box.send_keys(Keys.RETURN)
            search_box.submit()
            time.sleep(random_wait())
        #type the website directly
        if search == 1:
            self.browser.get("https://www.instagram.com/explore/tags/" + word)

def liking_pictures(browser0):
    browser0.implicitly_wait(5)

    browser = Interact(browser0)
    browser.word_search()
    browser.firstpic_click()

    browser.like_pic()
    browser.next_picture().click()
    browser.continue_liking()
    time.sleep(random_wait(10))


if __name__ == '__main__':
    with browse() as browser0:
        #unsubscribing(browser0)
        liking_pictures(browser0)
