import unittest
from selenium import webdriver
from ddt import unpack, ddt, data
import random

@ddt
class SmokeTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://popchest.io')

    def tearDown(self):
        self.driver.quit()

    def login(self, mail, pwd):
        self.driver.find_element_by_css_selector('#navbar .menu-link.login-link').click()
        email = self.driver.find_element_by_id('emailInput')
        email.clear()
        email.send_keys(mail)
        passwd = self.driver.find_element_by_id('passwordInput')
        passwd.clear()
        passwd.send_keys(pwd)
        self.driver.find_element_by_css_selector('.panel-body button.btn').click()

    def signup(self, mail, pwd):
        self.driver.find_element_by_css_selector('#navbar li.btn-join-us a').click()
        self.driver.find_element_by_css_selector('#checkPwned').click()
        email = self.driver.find_element_by_id('emailInput')
        email.clear()
        email.send_keys(mail)
        passwd = self.driver.find_element_by_id('passwordInput')
        passwd.clear()
        passwd.send_keys(pwd)
        self.driver.find_element_by_css_selector('.panel-body button.btn').click()

    def logout(self):
        self.driver.find_element_by_xpath('//*[@data-qa="header"]//div[@data-qa="drop-down-menu"]').click()
        self.driver.find_element_by_xpath(
            '//*[@data-qa="header"]//div[@data-qa="drop-down-menu"]//nav//menu[7]').click()
    ###
    ### helper methods todo move to another file
    ###
    def ensure_logout(self):
        return self.driver.find_element_by_xpath('//*[@data-qa="header"]//div[@data-qa="drop-down-menu"]')

    def ensure_login(self):
        return "/watch" in self.driver.current_url

    def ensure_signup(self):
        return "?welcome=beta" in self.driver.current_url

    def click_close_welcome_modal(self):
        self.driver.find_element_by_css_selector('#welcome-beta .modal-header button').click()

    def click_watch_welcome_modal(self):
        self.driver.find_element_by_css_selector('#welcome-beta .modal-footer button').click()

    def resent_notification(self):
        self.driver.find_element_by_partial_link_text('/account/reconfirm').click()

    def ensure_resend_notification(self):
        return self.driver.find_element_by_css_selector('.alert.alert-info').is_displayed()

    def upload_video(self, path_to_file):
        self.driver.find_element_by_css_selector('.dropzone').send_keys(path_to_file)

    def ensure_upload(self):
        return "/edit" in self.driver.current_url

    def fill_details(self, title, desc):
        details_title = self.driver.find_element_by_css_selector('.panel-body .form-group label[for="title"]')
        details_title.clear()
        details_title.send_keys(title)
        details_title = self.driver.find_element_by_css_selector('.panel-body .form-group label[for="description"]')
        details_title.clear()
        details_title.send_keys(desc)

    def video_price(self):
        tmp = self.driver.find_elements_by_css_selector('.price-options li')
        return tmp

    def set_video_price(self, amount):
        tmp = self.driver.find_elements_by_css_selector('.price-options li')
        if amount == 99:
            tmp[2].click()
        elif amount == 25:
            tmp[1].click()
        else:
            tmp[0].click()

    # decorator for random choice for pricing when uploading the video
    def random_pricing(video_price):
        def wrapper():
            random.choice(video_price).click

        return wrapper()


    def test_login(self, mail='grr@grr.la', pwd='1234qwe'):
        self.login(mail, pwd)
        if self.ensure_login():
            return True

    @unpack
    @data({'mail':'test2@distillery.com', 'pwd':'1234qwer'},
          {'mail': 'test3@distillery.com', 'pwd': ''},
          {'mail': '  ', 'pwd': 'qweasdq31'})
    @ unittest.SkipTest
    def test_signup(self, mail='hoehoehoe@grr.la', pwd='1234qwer'):
        self.signup(mail, pwd)
        if self.ensure_signup():
            return True

    def test_resend_notification(self):
        self.resent_notification()
        self.ensure_resend_notification()

    @unpack
    @data({'path_to_file': '/Users/bvrch/Downloads/SampleVideo_1280x720_20mb.mp4'},
          {'path_to_file': '/Users/bvrch/Downloads/SampleVideo_1280x720_10mb.mp4'},
          {'path_to_file': ''})
    def test_upload(self, path_to_file):
        self.upload_video(path_to_file)
        self.ensure_upload()




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SmokeTest)
    unittest.TextTestRunner(verbosity=2).run(suite)