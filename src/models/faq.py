from opf import db


class Faq(db.Model):
    __tablename__ = 'faq'
    id = db.Column(db.Integer, primary_key = True)
    question = db.Column(db.Text, nullable = False)
    answer = db.Column(db.Text, nullable = True)

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer