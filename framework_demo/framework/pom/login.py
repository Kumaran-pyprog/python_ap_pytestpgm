from selenium import webdriver

class Login():
    _username="username"
    _password="password"
    _login_button="//input[@type='submit']"
    _your_project="//*[contains(text(),'Your projects (0)')]"
    _installing_pkg="//a[contains(text(), 'Installing packages')]"
    _twitter_link="//a[contains(text(),'PyPI on Twitter')]"
    _twitter_url="https://twitter.com/PyPI"
    def __init__(self):
        global driver
        driver= webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
    def login_to_account(self):
        driver.get("https://pypi.org/account/login/")
        driver.find_element_by_id(self._username).send_keys("govind3011")
        driver.find_element_by_id(self._password).send_keys("govind@3011")
        driver.find_element_by_xpath(self._login_button).click()
        print("Login successfull")
    def verify_login(self):
        return driver.find_element_by_xpath(self._your_project).is_displayed()
    def verify_twitter_link(self):
        driver.find_element_by_xpath(self.verify_twitter_link()).is_displayed()
    def verify_twiiter_link(self):
        driver.find_element_by_xpath(self._twitter_link)


#Note: command to execute the code in gitbash
# git commit -m "first commit"
#git remote add origin https://github.com/Kumaran-pyprog/frameworkproj_demo.git
# git push origin master
#
