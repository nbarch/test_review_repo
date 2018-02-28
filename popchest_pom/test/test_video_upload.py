from popchest_pom.test.conftest import setup
from popchest_pom.pages.upload_page import *
from popchest_pom.pages.signup_page import *


def test_upload_video(setup):
    tmp = SignupHelper()
    tmp.login("test1@distillery.com", "1234qwer")
    upload = UploadHelper()
    upload.upload_video('/Users/bvrch/Downloads/SampleVideo_1280x720_10mb.mp4')


