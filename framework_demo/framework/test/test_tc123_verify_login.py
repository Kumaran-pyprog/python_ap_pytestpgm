from Demo.pom.login import Login
import pytest


@pytest.mark.usefixtures("oneTimeSetup", "setUp")
class TestClassDemo():
    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.log_in=Login()
        print("class Label set up of Py Pi Org")
        yield
        print("Logging out of Py Pi Org")
    def test_tc123_verify_login(self):
        assert self.log_in.login_to_account()
        assert self.log_in.verify_login()

