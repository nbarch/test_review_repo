import pytest
from popchest_pom.fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

# тестовый метод принимает в качестве параметра фикстуру
def test_login(app):
    app.session.login("mail", "pwd")

def test_signup(app):
    app.session.signup("mail", "pwd")
    if app.session.ensure_signup():
        return True

def test_upload(app):
    app.video.upload_by_click('path')

