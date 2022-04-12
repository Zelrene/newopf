from src.db_connector import DB_Connector

database = DB_Connector()

class AnnouncementsController():

    def create_announcement(self, announce_title, announce_descrip):

        database.insert_announcements(
           announce_title = announce_title,
           announce_descrip = announce_descrip
        )
        
    def get_announcement(self):
        announcements = database.select_announcements()
        return announcements

       