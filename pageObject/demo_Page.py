from selenium.webdriver.common.by import By
from Utility.custom_log import Log1


class DemoPage:
    username_xpath = "//input[@id='user-name']"
    password_xpath = "//input[@id='password']"
    login_button_xpath = "//input[@id='login-button']"
    menu_xpath = "//button[@id='react-burger-menu-btn']"
    logged_in_url = "https://www.saucedemo.com/inventory.html"
    logged_out_url = "https://www.saucedemo.com/"
    logout_xpath = "//a[@id='logout_sidebar_link']"

    logg = Log1.log1()

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.username_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def click_on_login(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def click_on_menu(self):
        self.driver.find_element(By.XPATH, self.menu_xpath).click()

    def click_on_logout(self):
        self.driver.find_element(By.XPATH, self.logout_xpath).click()

    def verify_login(self,username,password):
        currentUrl = self.driver.current_url
        if currentUrl == self.logged_in_url:
            self.logg.info("Login Successful with user " + username)
            assert True
        else:
            self.logg.info("Login Failed  with user "+ username)
            assert False

    def verify_logout(self):
        currentUrl = self.driver.current_url
        if currentUrl == self.logged_out_url:
            assert True
        else:
            assert False

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_on_login()
        self.verify_login(username,password)

    def logout(self):
        self.click_on_menu()
        self.click_on_logout()
        self.verify_logout()
