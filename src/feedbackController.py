
from src.db_connector import DB_Connector

database = DB_Connector()

class FeedbackController():

    def create_feedback(self, ticket_id, experience_rate, satisfied_level, additional_comments): 
        
        database.insert_feedback(
            ticket_id = ticket_id,
            experience_rate = experience_rate,
            satisfied_level = satisfied_level,
            additional_comments = additional_comments
        )
    
    def get_all_feedback(self):
        all_feedback = database.select_all_feedback()
        return all_feedback

    def get_single_feedback(self, feedback_id):
        feedback = database.select_single_feedback(feedback_id = feedback_id)
        return feedback

    def delete_feedback(self, feedback_id):
        database.delete_feedback(feedback_id = feedback_id)

