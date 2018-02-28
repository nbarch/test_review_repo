from popchest_pom.pages.base_page import Base


class UploadHelper(Base):
    def __init__(self):
        super().__init__()

    def retry_upload(self):
        self.driver.find_element_by_css_selector('.retry').click()

    def set_details(self, title, desc):
        self.driver.find_element_by_name('title').send_keys(title)
        self.driver.find_element_by_name('description').send_keys(desc)

    def click_upload(self):
        self.driver.find_element_by_css_selector('.upload-button').click()

    def upload_video(self, path_to_file):
        self.click_upload()
        # self.driver.find_element_by_css_selector('.dropzone').send_keys(path_to_file)
        _ = self.driver.find_element_by_css_selector('.studio-uploadernull .dropzone')
        _.click().send_keys(path_to_file)

    def ensure_upload(self):
        return "/edit" in self.driver.current_url

    def fill_details(self, title, desc):
        details_title = self.driver.find_element_by_name('title')
        details_title.clear()
        details_title.send_keys(title)
        details_title = self.driver.find_element_by_name('description')
        details_title.clear()
        details_title.send_keys(desc)

    def video_price(self):
        tmp = self.driver.find_elements_by_css_selector('.price-options li')
        return tmp

    #todo add custom price when logged in as an admin
    def set_video_price(self, amount):
        tmp = self.driver.find_elements_by_css_selector('.price-options li')
        if amount == 99:
            tmp[2].click()
        elif amount == 25:
            tmp[1].click()
        else:
            tmp[0].click()


