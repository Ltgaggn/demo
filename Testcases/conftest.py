import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=["chrome"])
def setup(request):
    opt = Options()
    opt.headless = False
    if request.param == 'chrome':
        opt.add_argument("--incognito")
        opt.add_argument("--window-size=1280,800")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
        print("*********Launching chrome browser******")
    elif request.param == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        print("*********Launching firefox browser******")
    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield
    driver.close()
#
# @pytest.fixture(params=["chrome"])
# def setup(request):
#     opt = Options()
#     opt.headless = True
#     if request.param == 'chrome':
#         opt.add_argument("--incognito")
#         opt.add_argument("--window-size=1280,800")
#         driver = webdriver.Remote(
#             command_executor='localhost:8080/wd/hub',
#             desired_capabilities=DesiredCapabilities.CHROME, options=opt)
#         print("*********Launching chrome browser******")
#     elif request.param == 'firefox':
#         driver = webdriver.Remote(
#             command_executor='http://172.17.0.1:4442/wd/hub',
#             desired_capabilities=DesiredCapabilities.FIREFOX)
#         print("*********Launching firefox browser******")
#     else:
#         driver = webdriver.Ie()
#         print("*********Launching ie browser******")
#     yield driver
