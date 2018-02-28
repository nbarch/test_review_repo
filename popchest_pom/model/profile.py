#todo review to use in profile_page.py
class Profile:
    def __init__(self, mail, fname, lname, bio, site, channel):
        self.mail = mail
        self.fname = fname
        self.lname = lname
        self.bio = bio
        self.site = site
        self.channel = channel

    @property
    def mail(self):
        return self.mail

    @mail.setter
    def mail(self, value):
        self.mail = value

    @property
    def fname(self):
        return self.fname

    @fname.setter
    def fname(self, value):
        self.fname = value

    @property
    def lname(self):
        return self.lname

    @lname.setter
    def lname(self, value):
        self.lname = value

    @property
    def bio(self):
        return self.bio

    @bio.setter
    def bio(self, value):
        self.bio = value

    @property
    def site(self):
        return self.site

    @site.setter
    def site(self, value):
        self.site = value

    @property
    def channel(self):
        return self.channel

    @channel.setter
    def channel(self, value):
        self.channel = value



