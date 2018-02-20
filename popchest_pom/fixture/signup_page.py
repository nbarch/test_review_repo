from popchest_pom.fixture.base import Page
from popchest_pom.locators import LoginPageLocators
from popchest_pom.test.tests_login_page import app


class SignupHelper:
    def __init__(self):
        self.app = app
        self.locator = LoginPageLocators

    def signup(self, mail, pwd):
        driver = self.app.driver
        driver.app.find_element(*self.locator.EMAIL).send_keys(mail)
        driver.app.find_element(*self.locator.PWD).send_keys(pwd)
        driver.app.find_element(*self.locator.JOIN).click()

    def click_terms_of_use(self):
        driver = self.app.driver
        driver.app.find_element(*self.locator.TERMS).click()

    def click_privacy_statement(self):
        driver = self.app.driver
        driver.app.find_element(*self.locator.PRIVACY).click()

    def join_with_twitter(self):
        driver = self.app.driver
        driver.app.find_element(*self.locator.JOIN_TWITTER).click()

    def join_with_facebook(self):
        driver = self.app.driver
        driver.app.find_element(*self.locator.JOIN_FB).click()

    def forgot_password(self, mail):
        driver = self.app.driver
        driver.app.find_element(*self.locator.FORGOT_PWD).click()
        driver.app.find_element(*self.locator.EMAIL_INPUT).send_keys(mail)
        driver.app.find_element(*self.locator.SUBMIT_BUTTON).click()

    def join_from_login(self):
        driver = self.app.driver
        driver.app.find_element(*self.locator.JOIN).click()

    def ensure_login(self):
        driver = self.app.driver
        return "/watch" in driver.app.current_url

    def ensure_signup(self):
        driver = self.app.driver
        return "?welcome=beta" in driver.app.current_url