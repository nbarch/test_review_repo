#todo review to use in upload_page.py
class Video:
    def __init__(self, title, desc):
        self.title = title
        self.desc = desc

    @property
    def title(self):
        return self.title

    @title.setter
    def title(self, value):
        self.title = value

    @property
    def desc(self):
        return self.desc

    @desc.setter
    def desc(self, value):
        self.desc = value
