import pytest
from popchest_pom.pages.webdriver_helper.helper import *
from popchest_pom.pages.signup_page import *
from popchest_pom.pages.single_video_page import *

# todo add error/exception processing for tests

@pytest.fixture(scope='session')
def setup(request):
    request.driver = driver_helper.get_webdriver()
    yield request.driver
    request.addfinalizer(driver_helper.tear_down)

#
# @pytest.fixture(scope="session")
# def logged_in(request):
#     request.driver = driver_helper.get_webdriver()
#     tmp = SignupHelper()
#     tmp.login("test1@distillery.com", "1234qwer")
#     yield request.driver
#     request.addfinalizer(driver_helper.tear_down)

# @pytest.fixture(scope="session")
# def open_video(request):
#     request.driver = driver_helper.get_webdriver()
#     tmp = SignupHelper()
#     tmp.login("test1@distillery.com", "1234qwer")
#     v = WatchVideoHelper()
#     v.select_video()
#     yield request.driver
#     request.addfinalizer(driver_helper.tear_down)
#

@pytest.fixture(scope="session")
def logged_in(setup):
    tmp = SignupHelper()
    tmp.login("test1@distillery.com", "1234qwer")


@pytest.fixture(scope="session")
def open_video(logged_in):
    v = WatchVideoHelper()
    v.select_video()