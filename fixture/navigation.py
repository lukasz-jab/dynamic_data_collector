class NavigationHelper:
    def __init__(self, app):
        self.app = app

    def open_home(self):
        wd = self.app.wd
        base_url = self.app.base_url
        wd.get(base_url)
