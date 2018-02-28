from popchest_pom.test.conftest import *
from popchest_pom.pages.signup_page import *


def test_login(setup):
    tmp = SignupHelper()
    tmp.login("test1@distillery.com", "1234qwer")
    tmp.ensure_login()

#todo import Faker to generate passwords
@pytest.mark.parametrize("mail, pwd",[
    ("test2@distillery.com", " "),
    ("test3@distillery.com", "213wqersdad"),
    (" ", " "),
])
def test_signin(setup, mail, pwd):
    tmp = SignupHelper()
    tmp.signup(mail, pwd)
    if tmp.ensure_signup():
        return True


def test_logout(logged_in):
    user = SignupHelper()
    user.logout()
    user.ensure_logout()