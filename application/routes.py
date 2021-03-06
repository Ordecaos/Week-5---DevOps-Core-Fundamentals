from flask import request, redirect, render_template
from application import app, db
from application.forms import Add_Player, Update_Player, Add_Campaign, Update_Campaign, Add_Book, Update_Book
from application.models import PlayersTable, CampaignsTable, BooksTable

#This file is what allows the HTML portion of the code to navigate between the various pages and processes. Everything from viewing the page to inputting new records, editing existing ones and deleting existing records.

@app.route('/')
def home():
    return render_template('Homepage.html')

@app.route('/Players')
def Player_Page():
    pla_id = PlayersTable.query.all()
    return render_template('Players.html', records=pla_id)

@app.route('/PlayerDetails/<int:Player_ID>')
def Player_Info(Player_ID):
    data = PlayersTable.query.filter_by(Player_ID=Player_ID).first()
    return render_template("Playerinfo.html", record=data)

@app.route('/Playerinput', methods=["GET", "POST"])
def Add_Players():
    form = Add_Player()
    if request.method == 'POST':
        Name=form.Player_name.data
        Character_Name=form.Character_Name.data
        Character_Level=form.Character_Level.data
        Character_Class=form.Character_Class.data
        Character_Race=form.Character_Race.data
        Campaign_In=form.Campaign_In.data
        NewPlayer = PlayersTable(Player_name=Name, Character_Name=Character_Name, Character_Level=Character_Level, Character_Class=Character_Class, Character_Race=Character_Race, Campaign_In=Campaign_In)
        db.session.add(NewPlayer)
        db.session.commit()
        return redirect("/Players")
    return render_template("Playerinput.html", form=form)

@app.route('/PlayerEdit/<int:Player_ID>', methods=["GET", "POST"])
def Edit_Player(Player_ID):
    form = Update_Player()
    pla = PlayersTable.query.filter_by(Player_ID=Player_ID).first()
    if request.method == 'POST':
        pla.Player_name=form.Player_name.data
        pla.Character_Name=form.Character_Name.data
        pla.Character_Level=form.Character_Level.data
        pla.Character_Class=form.Character_Class.data
        pla.Character_Race=form.Character_Race.data
        pla.Campaign_In=form.Campaign_In.data
        db.session.commit()
        return redirect("/Players")
    return render_template("Playerinput.html", form=form)

@app.route('/PlayerDelete/<int:Player_ID>')
def Delete_Player(Player_ID):
    pla = PlayersTable.query.filter_by(Player_ID=Player_ID).first()
    db.session.delete(pla)
    db.session.commit()
    return redirect("/Players")

@app.route('/Campaigns')
def Campaign_Page():
    cam_id = CampaignsTable.query.all()
    return render_template('Campaign.html', records=cam_id)

@app.route('/CampaignDetails/<int:Campaign_ID>')
def Campaign_Info(Campaign_ID):
    data = CampaignsTable.query.filter_by(Campaign_ID=Campaign_ID).first()
    return render_template("Campaigninfo.html", record=data)

@app.route('/Campaigninput', methods=["GET", "POST"])
def Add_Campaigns():
    form = Add_Campaign()
    if request.method == 'POST':
        Campaign_Name=form.Campaign_Name.data
        Campaign_Setting=form.Campaign_Setting.data
        No_of_Players=form.No_of_Players.data
        Books_Used=form.Books_Used.data
        NewCampaign = CampaignsTable(Campaign_Name=Campaign_Name, Campaign_Setting=Campaign_Setting, No_of_Players=No_of_Players, Books_Used=Books_Used)
        db.session.add(NewCampaign)
        db.session.commit()
        return redirect("/Campaigns")
    return render_template("Campaigninput.html", form=form)

@app.route('/CampaignEdit/<int:Campaign_ID>', methods=["GET", "POST"])
def Edit_Campaign(Campaign_ID):
    form = Update_Campaign()
    cam = CampaignsTable.query.filter_by(Campaign_ID=Campaign_ID).first()
    if request.method == 'POST':
        cam.Campaign_Name=form.Campaign_Name.data
        cam.Campaign_Setting=form.Campaign_Setting.data
        cam.No_of_Players=form.No_of_Players.data
        cam.Books_Used=form.Books_Used.data
        db.session.commit()
        return redirect("/Campaigns")
    return render_template("Campaigninput.html", form=form)

@app.route('/CampaignDelete/<int:Campaign_ID>')
def Delete_Campaign(Campaign_ID):
    cam = CampaignsTable.query.filter_by(Campaign_ID=Campaign_ID).first()
    db.session.delete(cam)
    db.session.commit()
    return redirect("/Campaigns")

@app.route('/Books')
def Book_Page():
    bo_id = BooksTable.query.all()
    return render_template('Books.html', records=bo_id)

@app.route('/BookDetails/<int:Book_ID>')
def Book_Info(Book_ID):
    data = BooksTable.query.filter_by(Book_ID=Book_ID).first()
    return render_template("Booksinfo.html", record=data)

@app.route('/Bookinput', methods=["GET", "POST"])
def Add_Books():
    form = Add_Book()
    if request.method == 'POST':
        Book_Name=form.Book_Name.data
        Book_Contents=form.Book_Contents.data
        NewBook = BooksTable(Book_Name=Book_Name, Book_Contents=Book_Contents)
        db.session.add(NewBook)
        db.session.commit()
        return redirect("/Books")
    return render_template("Booksinput.html", form=form)

@app.route('/BookEdit/<int:Book_ID>', methods=["GET", "POST"])
def Edit_Book(Book_ID):
    form = Update_Book()
    bo = BooksTable.query.filter_by(Book_ID=Book_ID).first()
    if request.method == 'POST':
        bo.Book_Name=form.Book_Name.data
        bo.Book_Contents=form.Book_Contents.data
        db.session.commit()
        return redirect("/Books")
    return render_template("Booksinput.html", form=form)

@app.route('/BookDelete/<int:Book_ID>')
def Delete_Book(Book_ID):
    bo = BooksTable.query.filter_by(Book_ID=Book_ID).first()
    db.session.delete(bo)
    db.session.commit()
    return redirect("/Books")
