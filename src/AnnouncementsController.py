
from src.db_connector import DB_Connector

from datetime import datetime

from src.models.announcements import Announcements

database = DB_Connector()

class AnnouncementsController():

    def create_announcement(self, announce_title, announce_descrip):

        submission_dateTime = datetime.now()

        database.insert_announcements(
           announce_title = announce_title,
           announce_descrip = announce_descrip,
           submission_dateTime = submission_dateTime
        )
        
    def get_announcement(self):
        announcements = database.select_announcements()
        return announcements

    def delete_announcment(self, announcement_id):
        database.delete_announcement(announcement_id = announcement_id)

    def update_annouce_title(self, announcement_id, new_title):
        database.update_announce_title(
            announcement_id = announcement_id, 
            new_title = new_title)
       
    def update_annouce_descrip(self, announcement_id, new_descrip):
        database.update_announce_descrip( 
            announcement_id = announcement_id, 
            new_descrip = new_descrip) 

    def update_annouce_info(self, announcement_id, new_title, new_descrip):
        database.update_announce_info(
            announcement_id = announcement_id, 
            new_title = new_title,
            new_descrip = new_descrip)

    def get_recent_announcement_submission_dateTime(self):
        announcements = database.select_announcements()
        submission_dates_list = []

        for a in announcements:
            submission_dates_list.append(a.submission_dateTime)
        
        now = datetime.now()
        if (len(submission_dates_list) > 0):

            recent_submission_date = max(submission_dates_list)
        else:
            recent_submission_date = None

        return recent_submission_date

    def get_announcement_with_matching_submitted_date(self, submission_dateTime):
        announcement = database.select_announcement_with_matching_submission_dateTime(submission_dateTime = submission_dateTime)
        return announcement