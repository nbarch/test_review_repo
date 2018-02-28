from popchest_pom.pages.base_page import Base


class ProfileHelper(Base):
    def __init__(self):
        super().__init__()

    def click_update(self):
        self.driver.find_element_by_css_selector('#editProfileForm .panel-footer button').click()

    # todo use Profile model to pass & set the arguments
    def update_form(self, mail, fname, lname, bio, site, channel):
        self.driver.find_element_by_id('emailInput').send_keys(mail)
        self.driver.find_element_by_id('firstnameInput').send_keys(fname)
        self.driver.find_element_by_id('lastnameInput').send_keys(lname)
        self.driver.find_element_by_id('aboutMe').send_keys(bio)
        self.driver.find_element_by_id('websiteInput').send_keys(site)
        self.driver.find_element_by_id('youtubeChannelId').send_keys(channel)
        self.driver.click_update()

    def set_link(self, username):
        self.driver.find_element_by_name('username').send_keys(username)
        self.driver.driver.click_update()

    def set_password(self, new_pwd, conf_pwd):
        self.driver.find_element_by_name('newPassword').send_keys(new_pwd)
        self.driver.find_element_by_name('confirmNewPassword').send_keys(conf_pwd)
        self.driver.click_update()

    def set_wallet_addr(self, addr):
        self.driver.find_element_by_name('payoutAddress').send_keys(addr)
        self.driver.click_update()
