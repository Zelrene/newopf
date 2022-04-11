from sqlalchemy import false, true
from src.db_connector import DB_Connector

database = DB_Connector()

class UserController(): 

    def create_user(self, first_name, last_name, user_role, contact_email, net_id, gender, student_year, password): 
        
        if gender == 'Male':
            gender = 'M'
        elif gender == 'Female':
            gender = 'F'
        else:
            gender = 'NA'

        database.insert_user(
            first_name = first_name, 
            last_name = last_name,
            user_role = user_role,
            contact_email = contact_email,
            net_id = net_id,
            gender = gender,
            student_year = student_year,
            password = password
            )

    def get_all_users(self):
        users = database.select_all_tickets()
        return users


    def get_user_info_with_matching_email(self, contact_email):
        user_info = database.select_user_with_matching_email(contact_email)
        return user_info

    def get_user_info_with_matching_netid(self, net_id):
        user_info = database.select_user_with_matching_netid(net_id)
        return user_info

    def get_password_with_matching_email(self, contact_email):
        password = database.select_password_with_matching_email(contact_email)
        return password
        

    def get_password_with_matching_netid(self, net_id):
        password = database.select_password_with_matching_netid(net_id)
        return password


    def get_first_name_with_matching_email(self, contact_email):
        first_name = database.select_first_name_with_matching_email(contact_email)
        return first_name

    def get_first_name_with_matching_netid(self, net_id):
        first_name = database.select_first_name_with_matching_netid(net_id)
        return first_name

    def get_last_name_with_matching_email(contact_email):
        last_name = database.select_last_name_with_matching_email(contact_email)
        return last_name

    def get_last_name_with_matching_netid(self, net_id):
        last_name = database.select_last_name_with_matching_netid(net_id)
        return last_name

    def get_firstLast_name_with_matching_email(self, contact_email):
        first_name = self.get_first_name_with_matching_email(contact_email)
        last_name = self.get_last_name_with_matching_email(contact_email)
        name = first_name + " " + last_name
        return name

    def get_firstLast_name_with_matching_netid(self, net_id):
        first_name = self.get_first_name_with_matching_netid(net_id)
        last_name = self.get_last_name_with_matching_netid(net_id)
        name = first_name + " " + last_name
        return name

    def check_user_with_email_exist(self, contact_email):
        #will check if a user with given email already exists in the db
        #if user exists, return true
        #else return false
        user = database.select_user_with_matching_email(contact_email)
        if user:
            return True
        else:
            return False

    def check_user_with_netid_exist(self, net_id):
        #will check if a user with given netid already exists in the db
        #if user exists, return true
        #else return false
        user = database.select_user_with_matching_netid(net_id)
        if user:
            return True
        else:
            return False

    def get_role_with_matching_email(self, contact_email):
        role = database.select_role_with_matching_email(contact_email)
        return role

    def get_role_with_matching_netid(self, net_id):
        role = database.select_role_with_matching_netid(net_id)
        return role    

    def is_user_admin(self, net_id):
        role = database.select_role_with_matching_netid(net_id)

        if role == 'Admin':
            return True
        else:
            return False

    
    def get_resident_num_with_matching_gender(self, gender):
        resident_num = database.get_residents_num_with_matching_gender(gender = gender)
        return resident_num

    def get_resident_num_with_matching_genders(self, genders):
        genders = genders
        total_residents = []
        
        for gender in genders:
            resident_num = self.get_resident_num_with_matching_gender(gender)
            total_residents.append(resident_num)
            
        return total_residents

        