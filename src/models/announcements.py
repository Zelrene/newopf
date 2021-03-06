
from opf import db


class Announcements(db.Model):
    __tablename__ = 'announcements'
    id = db.Column(db.Integer, primary_key = True)
    announce_title = db.Column(db.Text, nullable = False)
    announce_descrip = db.Column(db.Text, nullable = False)
    submission_dateTime = db.Column(db.DateTime, nullable = False)
    
    def __init__(self, announce_title, announce_descrip, submission_dateTime):
        self.announce_title = announce_title
        self.announce_descrip = announce_descrip
        self.submission_dateTime = submission_dateTime
      
