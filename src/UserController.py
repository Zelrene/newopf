from src.db_connector import DB_Connector

database = DB_Connector()

class UserController(): 

    def create_user(self, first_name, last_name, isStudent, contact_email, net_id, nshe_id, gender, year, password): 

        if isStudent == 'Student':
            isStudent = True
        else:
            isStudent = False

        if gender == 'Male':
            gender = 'M'
        elif gender == 'Female':
            gender = 'F'
        else:
            gender = 'F'

        database.insert_user(first_name, last_name, isStudent, contact_email, net_id, nshe_id, gender, year, password)
