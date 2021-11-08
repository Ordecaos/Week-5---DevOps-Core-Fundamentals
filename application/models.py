from application import db

class PlayersTable(db.Model):
    __tablename__ = 'PlayerTable'
    Player_ID = db.Column(db.Integer, primary_key = True)
    Player_name = db.Column(db.String(255))
    Character_Name = db.Column(db.String(255))
    Character_Level = db.Column(db.Integer)
    Character_Class = db.Column(db.String(255))
    Character_Race = db.Column(db.String(255))
    #Campaign_In = db.Column(db.Integer, db.ForeignKey('campaignsTable.Campaign_ID'))
    
class CampaignsTable(db.Model):
    __tablename__ = 'CampaignTable'
    Campaign_ID = db.Column(db.Integer, primary_key = True)
    Campaign_Name = db.Column(db.String(255))
    Campaign_Setting = db.Column(db.String(255))
    No_of_Players = db.Column(db.Integer)
    #Books_Used = db.Column(db.Integer, db.ForeignKey('booksTable.Book_ID'))
    #Players_rel = db.relationship('PlayersTable', backref='campaign')


class BooksTable(db.Model):
    __tablename__ = 'BooksTable'
    Book_ID = db.Column(db.Integer, primary_key = True)
    Book_Name = db.Column(db.String(255))
    Book_Contents = db.Column(db.String(255))
    #Campaigns_rel = db.relationship('CampaignsTable', backref='book')