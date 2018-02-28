from popchest_pom.pages.base_page import Base


class SignupHelper(Base):
    def __init__(self):
        super().__init__()

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
        self.driver.find_element_by_css_selector('.dropdown-toggle.transition').click()
        self.driver.find_element_by_xpath(
            '//*[@data-qa="header"]//div[@data-qa="drop-down-menu"]//nav//menu[7]').click()

    def click_terms_of_use(self):
        self.driver.find_element_by_css_selector('.checkbox a[href="/terms-of-use"]').click()

    def click_privacy_statement(self):
        self.driver.find_element_by_css_selector('.checkbox a[href="/privacy-policy"]').click()

    def join_with_twitter(self):
        self.driver.find_element_by_css_selector('.connect-twitter.login a').click()

    def join_with_facebook(self):
        self.driver.find_element_by_css_selector('.connect-facebook.login a').click()

    def forgot_password(self, mail):
        self.driver.find_element_by_css_selector('.forgot-password-link').click()
        self.driver.find_element_by_name('email').send_keys(mail)
        self.driver.find_element_by_css_selector('button[type="submit"]').click()

    def join_from_login(self):
        self.driver.find_element_by_css_selector('.text-center.bottom-extra a').click()

    def ensure_login(self):
        return "/watch" in self.driver.current_url

    def ensure_signup(self):
        return "?welcome=beta" in self.driver.current_url

    def ensure_logout(self):
        return self.driver.find_element_by_xpath('//*[@data-qa="header"]//div[@data-qa="drop-down-menu"]')

