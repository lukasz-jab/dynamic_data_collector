from selenium import webdriver

from fixture.navigation import NavigationHelper
from fixture.session import SessionHelper


class Application:
    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.base_url = base_url
        self.wd.implicitly_wait(3)
        self.session = SessionHelper(self)
        self.navigation = NavigationHelper(self)

    def destroy(self):
        self.wd.quit()
