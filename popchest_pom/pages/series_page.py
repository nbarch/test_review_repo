from popchest_pom.pages.base_page import Base


class Series(Base):
    def __init__(self):
        super().__init__()

    def go_to_series_page(self):
        #todo review

    def add_series(self):
        self.driver.find_element_by_css_selector('button.btn').click()

    def ensure_series_page(self):
        return "/studio/series/new" in self.driver.current_url

    #todo review
    def select_series_category(self, category):
        dropdown = {'Comedy': 'react-select-2--option-0',
                    'Tech': 'react-select-2--option-1',
                    'Politics': 'react-select-2--option-2',
                    'Cinema': 'react-select-2--option-3',
                    'Gaming': 'react-select-2--option-4',
                    'Feature Film': 'react-select-2--option-5',
                    'Short Film': 'react-select-2--option-6',
                    'Web Series': 'react-select-2--option-7'
                    }
        self.driver.find_element_by_css_selector('.Select-placeholder').send_keys(*dropdown[category])

    def create_series(self, title, desc, price):
        tmp_title = self.driver.find_element_by_xpath('//div[@class="form-group"]/input[@class="form-control"]')
        tmp_title.clear()
        tmp_title.send_keys(title)

        tmp_desc = self.driver.find_element_by_xpath('//div//textarea')
        tmp_desc.clear()
        tmp_desc.send_keys(desc)

        tmp_price = self.driver.find_element_by_css_selector('input.price-field')
        tmp_price.clear()
        tmp_price.send_keys(price)

    def search_series_video(self, text):
        input = self.driver.find_element_by_css_selector('input.form-control.search-input')
        input.clear()
        input.send_keys(text)
        input.send_keys(Keys.ENTER)

    def select_video_from_list(self):
        videos = self.driver.find_elements_by_css_selector('.video-list-editor li'):
        return random.choice(videos).click()

    def change_privacy(self):
        self.driver.find_element_by_css_selector('.privacy-container .react-toggle-thumb').click()

    def create_series(self):
        self.driver.find_element_by_css_selector('button.save-bundle-btn').click()

    def cancel_creation(self):
        self.driver.find_element_by_css_selector('.cancel-container').click()

    def click_edit_series(self):
        self.driver.find_element_by_css_selector('.editButton').click()
