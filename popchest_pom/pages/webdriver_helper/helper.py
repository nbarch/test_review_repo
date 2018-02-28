from selenium import webdriver


class WebdriverHelper(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get('https://popchest.io')

    def get_webdriver(self):
        return self.driver

    def tear_down(self):
        self.driver.quit()


driver_helper = WebdriverHelper()