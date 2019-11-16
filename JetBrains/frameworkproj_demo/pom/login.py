from selenium import webdriver

class Login():
    _username="username"
    _password="password"
    _login_button="//input[@type='submit']"
    _your_project="//*[contains(text(),'Your projects (0)')]"
    def __init__(self):
        global driver
        driver=webdriver.Chrome()
    def login_to_account(self):
        driver.get("https://pypi.org/account/login/")
        driver.find_element_by_id(self._username).send_keys("ashok")
        driver.find_element_by_id(self._password).send_keys("ashok123")
        driver.find_element_by_xpath(self._login_button).click()
        print("Login successfull")
    def verify_login(self):
        return driver.find_element_by_xpath(self._your_project).is_displayed()


