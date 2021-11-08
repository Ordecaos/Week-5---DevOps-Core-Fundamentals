from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField, SubmitField

class Add_Player(FlaskForm):
    
    Player_name = StringField("Your Name")
    Character_Name = StringField("Character Name")
    Character_Level = SelectField("Character Level", choices=[(1), (2), (3), (4), (5), (6), (7), (8), (9), (10), (11), (12), (13), (14), (15), (16), (17), (18), (19), (20)])
    Character_Class = SelectField("Character Class", choices=[('Artificer', 'artificer'), ('Barbarian', 'barbarian'), ('Bard', 'bard'), ('Blood Hunter', 'blood hunter'), ('Cleric', 'cleric'), ('Druid', 'druid'), ('Fighter', 'fighter'), ('Monk', 'monk'), ('Paladin', 'paladin'), ('Ranger', 'ranger'), ('Rogue', 'rogue'), ('Sorcerer', 'sorcerer'), ('Warlock', 'warlock'), ('Wizard', 'wizard')])
    Character_Race = StringField("Character Race")
    Campaign_In = IntegerField("Enter the Campaign ID")
    submit = SubmitField("Add Player")

class Update_Player(FlaskForm):

    Player_name = StringField("Your Name")
    Character_Name = StringField("Character Name")
    Character_Level = SelectField("Character Level", choices=[(1), (2), (3), (4), (5), (6), (7), (8), (9), (10), (11), (12), (13), (14), (15), (16), (17), (18), (19), (20)])
    Character_Class = SelectField("Character Class", choices=[('Artificer', 'artificer'), ('Barbarian', 'barbarian'), ('Bard', 'bard'), ('Blood Hunter', 'blood hunter'), ('Cleric', 'cleric'), ('Druid', 'druid'), ('Fighter', 'fighter'), ('Monk', 'monk'), ('Paladin', 'paladin'), ('Ranger', 'ranger'), ('Rogue', 'rogue'), ('Sorcerer', 'sorcerer'), ('Warlock', 'warlock'), ('Wizard', 'wizard')])
    Character_Race = StringField("Character Race")
    Campaign_In = IntegerField("Enter the Campaign ID")
    submit = SubmitField("Update Player")

class Add_Campaign(FlaskForm):

    Campaign_Name = StringField("The Campaign Name")
    Campaign_Setting = StringField("The Setting of the Campaign")
    No_of_Players = SelectField("Choose the number of players", choices=[(1), (2), (3), (4), (5), (6), (7), (8), (9), (10)])
    Books_Used = IntegerField("Enter the Book ID")
    submit = SubmitField("Add Campaign")

class Update_Campaign(FlaskForm):

    Campaign_Name = StringField("The Campaign Name")
    Campaign_Setting = StringField("The Setting of the Campaign")
    No_of_Players = SelectField("Choose the number of players", choices=[(1), (2), (3), (4), (5), (6), (7), (8), (9), (10)])
    Books_Used = IntegerField("Enter the Book ID")
    submit = SubmitField("Add Campaign")

class Add_Book(FlaskForm):

    Book_Name = StringField("The Books Name")
    Book_Contents = StringField("Enter the contents of the book")
    submit = SubmitField("Add Book")

class Update_Book(FlaskForm):

    Book_Name = StringField("The Books Name")
    Book_Contents = StringField("Enter the contents of the book")
    submit = SubmitField("Add Book")