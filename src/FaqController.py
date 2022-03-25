from src.db_connector import DB_Connector

database = DB_Connector()

class FaqController():
    
    def create_faq(self, question, answer):
        database.insert_faq(
            question = question,
            answer = answer)

    def get_all_faq(self):
        faqs = database.select_all_faq()
        return faqs

    def delete_faq(self, faq_id):
        database.delete_faq(faq_id)