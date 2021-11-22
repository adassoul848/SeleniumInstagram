import selenium.common.exceptions
from initial_page import Browser, browse
from liking_all_pictures import Interact
import time
from bs4 import BeautifulSoup as bs

class Interact(Browser):

    def go_to_profil(self):
        time.sleep(2)
        #profile_name = input()
        profile_name = "dassouli_ym"
        self.browser.get("https://www.instagram.com/"+ profile_name +"/")

    def followers_and_following(self):
        result=[]
        '''follow = self.browser.find_elements_by_class_name("_9AhH0")
        soups = [bs(followw.get_attribute('innerHTML'), 'html.parser') for followw in follow]
        print(len(soups))
        for i in range(len(soups)):
            print(soups[i])
            if (soups[i].find('span')['title'] == "509"):
                result[0] = follow[i]
            elif (soups[i].find('a')['href'] == "/dassouli_ym/following/"):
                result[1] = follow[i]
        print(result)
        '''
        self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[3]/a/div/div[2]').click()
        return result
    '''
    //*[@id="react-root"]/section/main/div/ul/li[2] no
    //*[@id="react-root"]/section/main/div/ul/li[2]/a/span no
    //*[@id="react-root"]/section/main/div/ul/li[2]/a
    '''
    def unfollow(self):
        self.browser.find_element_by_partial_link_text("following").click()
        removes = self.browser.find_elements_by_xpath("//*[text()='Following']")
        print(removes)
        for remove in removes:
            time.sleep(1)
            remove.click()

    def make_them_unfollow(self):
        self.browser.find_element_by_partial_link_text("follower").click()
        removes = self.browser.find_elements_by_xpath("//*[text()='remove']")
        print(removes)
        for remove in removes:
            time.sleep()
            remove.click()


def unsubscribing(browser0):
    browser0.implicitly_wait(5)
    browser = Interact(browser0)
    browser.go_to_profil()
    browser.unfollow()
'''
    
    browser.followers_and_following()
'''

    #followers, following = browser.followers_and_following()
    #followers.click()

if __name__ == '__main__':
    with browse() as browser0:
        unsubscribing(browser0)

