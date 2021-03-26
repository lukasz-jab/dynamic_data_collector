from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException


class SessionHelper:
    def __init__(self, app):
        self.app = app

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert().accept()
        except NoAlertPresentException as e:
            return False
        return True
