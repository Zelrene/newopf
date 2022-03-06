

import string


class tickets(object):
    '''
    A class to represent the ticket data
    '''

    def __init__(self, title:string, description: string, location: string, building: string, unit: string, contact: string, additionalNotes: string):
        self.title = title
        self.description = description
        self.location = location
        self.building = building
        self.unit = unit
        self.contact = contact
        self.additionalNotes = additionalNotes

    


