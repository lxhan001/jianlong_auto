from selenium import webdriver
import time


class Base:
    def __init__(self):
        self.driver = webdriver.Chrome(r'D:\chromdriver\chromedriver.exe')
        self.driver.get('https://jianlong.test.spdio.com/outer/loginaccount')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def base_find_element(self, loc):
        return self.driver.find_element(*loc)

    def base_click_button(self, loc):
        self.base_find_element(loc).click()

    def base_send_keys(self, loc, text):
        self.base_find_element(loc).clear()
        self.base_find_element(loc).send_keys(text)

    def base_get_text(self, loc):
        return self.base_find_element(loc).text

    def base_get_img(self):
        self.driver.get_screenshot_as_file('../Img/{}.png'.format(time.strftime('%Y_%m_%d_%H_%M_%S')))
