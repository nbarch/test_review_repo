from selenium import webdriver
from selenium.webdriver import ActionChains
from popchest_pom.fixture.profile_page import ProfileHelper
from popchest_pom.fixture.upload_helper import UploadHelper
from popchest_pom.fixture.signup_page import SignupHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.locator = #todo review
        self.session = ProfileHelper(self)
        self.signup = SignupHelper(self)
        self.video = UploadHelper(self)

    def open_homepage(self):
        self.driver.get('https://popchest.io')

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def destroy(self):
        self.driver.quit()

    def hover(self=None, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self).move_to_element(element)
        hover.perform()
