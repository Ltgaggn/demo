import pytest

from pageObject.GFG_paramiko import MachinePerformance
from pageObject.demo_Page import DemoPage


@pytest.mark.usefixtures("setup")
class BaseClass:
    pass


class TestDemo(BaseClass):

    @pytest.mark.ui
    @pytest.mark.parametrize("username,password", [
        ("standard_user", "secret_sauce"),
        ("standard_user","standard_user")
    ]
                             )
    def test_login(self, username, password):
        self.driver.get("https://www.saucedemo.com/")
        self.lg = DemoPage(self.driver)
        self.lg.login(username, password)

    @pytest.mark.parametrize("username,password", [
        ("standard_user", "secret_sauce")
    ]
                             )
    def test_logout(self, username, password):
        self.driver.get("https://www.saucedemo.com/")
        self.lg = DemoPage(self.driver)
        self.lg.login(username, password)
        self.lg.logout()
