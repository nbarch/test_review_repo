from popchest_pom.pages.base_page import Base
import random

class WatchVideoHelper(Base):

    def __init__(self):
        super().__init__()

    def select_video(self):
        videos = self.driver.find_elements_by_css_selector('.video-list .video-list-item')
        random.choice(videos).click()

    def click_play_pause(self):
        self.driver.find_element_by_css_selector('#video-display #video_player .vjs-big-play-button')

    def click_share_on_video(self):
        self.driver.find_element_by_css_selector('.share-links .share').click()

    def click_vote_on_video(self):
        self.driver.find_element_by_css_selector('.share-links .vote .fa.fa-heart').click()

    def click_skip_preview(self):
        self.driver.find_element_by_css_selector('#skip-preview-overlay').click()

    def click_mute(self):
        self.driver.find_element_by_css_selector('.vjs-control-bar .vjs-volume-menu-button').click()

    def choose_resolution(self):
        self.driver.find_elements_by_css_selector('.vjs-menu .vjs-menu-content li.vjs-menu-item')

    def click_fullscreen(self):
        self.driver.find_element_by_css_selector('.vjs-control-bar .vjs-fullscreen-control ').click()

    def click_logo_control_bar(self):
        self.driver.find_element_by_css_selector('.vjs-control-bar .vjs-control.vjs-button.logo').click()

    def ensure_redirect_from_video(self):
        return "https://popchest.com/" == self.driver.current_url

    def click_category(self):
        self.driver.find_element_by_css_selector('.video-bar .video-category a').click()

    def click_like(self):
        self.driver.find_element_by_css_selector('.video-actions .action-vote').click()

    def click_share(self):
        self.driver.find_element_by_css_selector('.video-actions .action-share').click()

    def click_edit(self):
        """ only if user is admin or own the video """
        self.driver.find_element_by_css_selector('.video-actions .action-edit').click()

    def click_creators_avatar(self):
        self.driver.find_element_by_css_selector('.video-details .artist-avatar').click()

    def click_creators_name(self):
        self.driver.find_element_by_css_selector('.video-details .artist-name a').click()

    def click_follow(self):
        self.driver.find_element_by_css_selector('.video-details .action-follow').click()

    def ensure_follow(self):
        return self.driver.find_element_by_css_selector('.video-details .action-follow.followed')

    def click_subscribe(self):
        self.driver.find_element_by_css_selector('.yt-uix-button ').click()

    def get_related_list(self):
        return self.driver.find_elements_by_css_selector('.featured-videos-sidebar ul.video-list li.video-list-item')

    def post_comment(self, text):
        self.driver.find_element_by_css_selector('#open-comments .js-comment-input').send_keys(text)
        self.driver.find_element_by_css_selector('#open-comments button').click()