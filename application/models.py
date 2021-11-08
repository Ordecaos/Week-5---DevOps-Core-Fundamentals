from application import db

class Players(db.Model):
    Player_ID = db.Column(db.Integer, primary_key = True)
    Player_name = db.Column(db.String(255))
    Character_Name = db.Column(db.String(255))
    Character_Level = db.Column(db.Integer(2))
    Character_Class = db.Column(db.String(255))
    Character_Race = db.Column(db.String(255))
    Campaign = db.Column(db.Integer,  db.ForeignKeys == 'campaigns.Campaign_ID')

class Campaigns(db.Model):
    Campaign_ID = db.Column(db.Integer, primary_key = True)
    Campaign_Name = db.Column(db.String(255))
    Campaign_Setting = db.Column(db.String(255))
    No_of_Players = db.Column(db.Integer)
    Books_Used = db.Column(db.Integer, db.ForeignKeys == 'books.Book_ID')
    Players = db.relationship('Players', backref='campaign')

class Books(db.Model):
    Book_ID = db.Column(db.Integer, primary_key = True)
    Book_Name = db.Column(db.String(255))
    Book_Contents = db.Column(db.String(255))
    Campaigns = db.relationship('Campaigns', backref='book')