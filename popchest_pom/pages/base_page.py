from popchest_pom.pages.webdriver_helper.helper import driver_helper


class Base:
    def __init__(self):
        self.driver = driver_helper.get_webdriver()
