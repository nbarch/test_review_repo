import os
from popchest_pom.locators import UploadVideoLocators
from selenium import webdriver


class UploadHelper:
    def __init__(self, app):
        self.app = app
        self.locator = UploadVideoLocators

    def upload_by_click(self, file):
        driver = self.app.driver
        # todo drop file review
        driver.app.find_element(*self.locator.DROPZONE).send_keys(os.getcwd() + file)

    def retry_upload(self):
        driver = self.app.driver
        driver.app.find_element(*self.locator.UPDATE).click()

    def set_details(self, title, desc):
        driver = self.app.driver
        driver.app.find_element(*self.locator.DETAILS['TITLE']).send_keys(title)
        driver.app.find_element(*self.locator.DETAILS['CATEGORY']).send_keys(desc)

