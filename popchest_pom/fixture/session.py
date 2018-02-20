class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, mail, pwd):
        driver = self.app.driver
        self.app.open()
        mail_tmp = driver.app.find_element(*driver.locator.EMAIL).clear()
        mail_tmp.send_keys(mail)
        pwd_tmp = driver.app.find_element(*driver.locator.PWD).clear()
        pwd_tmp.send_keys(pwd)
        driver.app.find_element(*driver.locator.LOGIN).click()
