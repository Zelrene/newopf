from view import db

import string

'''
class Ticket(db.Model):

    id = db.column()
    
    A class to represent the ticket data
    

    def __init__(self, title:string, description: string, location: string, building: string, unit: string, contact: string, additionalNotes: string):
        self.title = title
        self.description = description
        self.location = location
        self.building = building
        self.unit = unit
        self.contact = contact
        self.additionalNotes = additionalNotes
'''
    
class Ticket(db.Model):
    __tablename__ = 'ticket'
    id = db.Column(db.Integer, primary_key = True)
    #creator_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable = False)
    status = db.Column(db.String(25), nullable = False)
    severity_level = db.Column(db.String(50), nullable = False)
    description = db.Column(db.Text, nullable = False)
    building = db.Column(db.String(25), nullable = False)
    unit = db.Column(db.String(25), nullable = False)
    title = db.Column(db.String(75), nullable = False)
    location = db.Column(db.String(50), nullable = False)
    additionalNotes = db.Column(db.Text, nullable = True)
    contact = db.Column(db.Text, nullable = True)
    
    def __init__(self, status, severity_level, description, building, unit, title, location, additionalNotes, contact):
        self.status = status
        self.severity_level = severity_level
        self.description = description
        self.building = building
        self.unit = unit
        self. title = title
        self.location = location
        self.additionalNotes = additionalNotes
        self.contact = contact  

