from popchest_pom.test.conftest import *
from popchest_pom.pages.single_video_page import *


def test_open_video(logged_in):
    vid = WatchVideoHelper()
    vid.select_video()
    vid.click_play_pause()
    vid.click_play_pause()


def test_fullscreen(open_video):
    vid = WatchVideoHelper()
    vid.click_fullscreen()


def test_share_on_video(open_video):
    vid = WatchVideoHelper()
    vid.click_share_on_video()


def test_goto_category(open_video):
    vid = WatchVideoHelper()
    vid.click_category()


def test_goto_creator(open_video):
    vid = WatchVideoHelper()
    vid.click_creators_avatar()


def test_goto_creator(open_video):
    vid = WatchVideoHelper()
    vid.click_creators_name()


def test_click_follow(open_video):
    vid = WatchVideoHelper()
    vid.click_follow()
    vid.ensure_follow()


def test_vote_on_video(open_video):
    vid = WatchVideoHelper()
    vid.select_video()


@pytest.mark.parametrize("text", [
    (' '),
    ('Test comment'),
    ('Very big and long string that never ends, let\'s see how this affects comments section')
])
def test_post_comment(open_video, text):
    vid = WatchVideoHelper()
    vid.post_comment(text)
    vid.select_video()