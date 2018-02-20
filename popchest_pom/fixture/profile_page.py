from popchest_pom.fixture.base import Page
from popchest_pom.locators import ProfilePageLocators
from popchest_pom.test.conftest import app


class ProfileHelper:
    def __init__(self):
        self.app = app
        self.locator = ProfilePageLocators

    def click_update(self):
        driver = self.app.driver
        driver.app.find_element(self.locator.UPDATE).click()

    def update_form(self, email, fname, lname, bio, site, channel):
        driver = self.app.driver
        driver.app.find_element(*self.locator.PROFILE['EMAIL']).send_keys(email)
        driver.app.find_element(*self.locator.PROFILE['FIRST_NAME']).send_keys(fname)
        driver.app.find_element(*self.locator.PROFILE['LAST_NAME']).send_keys(lname)
        driver.app.find_element(*self.locator.PROFILE['BIO']).send_keys(bio)
        driver.app.find_element(*self.locator.PROFILE['WEBSITE']).send_keys(site)
        driver.app.find_element(*self.locator.PROFILE['YOUTUBE']).send_keys(channel)
        driver.app.click_update()

    def set_link(self, username):
        driver = self.app.driver
        driver.app.find_element(*self.locator.USERNAME).send_keys(username)
        driver.app.click_update()

    def set_password(self, new_pwd, conf_pwd):
        driver = self.app.driver
        driver.app.find_element(*self.locator.NEW_PWD).send_keys(new_pwd)
        driver.app.find_element(*self.locator.CONF_NEW_PWD).send_keys(conf_pwd)
        driver.app.click_update()

    def set_wallet_addr(self, addr):
        driver = self.app.driver
        driver.app.find_element(*self.locator.BTC_ADDR).send_keys(addr)
        driver.app.click_update()


