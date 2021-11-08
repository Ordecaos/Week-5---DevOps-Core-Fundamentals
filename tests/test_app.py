from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Players, Campaigns, Books
from application.form import Add_Player, Update_Player, Add_Campaign, Update_Campaign, Add_Book, Update_Book
import application.routes
from os import getenv

class TestGen(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI='db_uri',
        SECRET_KEY='TEST_SECRET_KEY',
        DEBUG=True,
        WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        db.create_all()
        Pl_sample = Players(Player_name='Jack', Character_Name='Paravax', Character_Level=16, Character_Class='Wizard', Character_Race='Dragonborn', Campaign=1)
        Ca_sample = Campaigns(Campaign_Name='Cities of Chrey', Campaign_Setting='Medival', No_of_Players=1, Books_Used=1)
        Bo_sample = Books(Book_Name='Dungeon Masters Guide', Book_Contents='Rules')
        db.session.add(Pl_sample)
        db.session.add(Ca_sample)
        db.session.add(Bo_sample)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class Pla_Tests(TestGen):
    def test_pla_get(self):
        response = self.client.get(url_for('Player_Page'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Jack', response.data)
    
    def test_cam_get(self):
        response = self.client.get(url_for('Campaign_Page'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Cities of Chrey', response.data)

    def test_bo_get(self):
        response = self.client.get(url_for('Book_Page'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Dungeon Masters Guide', response.data)

    def test_add_pla(self):
        response = self.client.post(
            url_for('Add_Player'),
            data = dict(Player_name='David', Character_Name='Devon', Character_Level=3, Character_Class='Artificer', Character_Race='Human', Campaign=1)
            follow_redirects = True)
        self.assertIn(b'David', response.data)

    def test_add_cam(self):
        response = self.client.post(
            url_for('Add_Campaign'),
            data = dict(Campaign_Name='Dark Visions', Campaign_Setting='High Tech', No_of_Players=1, Books_Used=1)
            follow_redirects = True)
        self.assertIn(b'Dark Visions', response.data)

    def test_add_bo(self):
        response = self.client.post(
            url_for('Add_Book'),
            data = dict(Book_Name='Tasha', Book_Contents='Spells')
            follow_redirects = True)
        self.assertIn(b'Tasha', response.data)
    
    def test_update_pla(self):
        response = self.client.post(
            url_for('Player_Edit', Player_ID=1),
            data = dict(Player_name='Luke', Character_Name='Balraz', Character_Level=3, Character_Class='Paladin', Character_Race='Dragonborn', Campaign=1)
            follow_redirects = True)
        self.assertIn(b'Luke', response.data)

    def test_update_cam(self):
        response = self.client.post(
            url_for('Campaign_Edit', Campaign_ID=1),
            data = dict(Campaign_Name='Night Skies', Campaign_Setting='Low Fantasy', No_of_Players=1, Books_Used=1)
            follow_redirects = True)
        self.assertIn(b'Night Skies', response.data)
        
    def test_update_bo(self):
        response = self.client.post(
            url_for('Book_Edit', Book_ID=1),
            data = dict(Book_Name='Ravnica', Book_Contents='Setting')
            follow_redirects = True)
        self.assertIn(b'Ravnica', response.data)

    def test_del_pla(self):
        response = self.client.get(url_for('Delete_Player', Player_ID = 1) follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Player Information', response.data)

    def test_del_cam(self):
        response = self.client.get(url_for('Delete_Campaign', Campaign_ID = 1) follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Campaign Information', response.data)

    def test_del_bo(self):
        response = self.client.get(url_for('Delete_Book', Book_ID = 1) follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Book Information', response.data)

    def test_pla_info(self):
        response = self.client.get(url_for('Player_Info', Player_ID=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Jack', response.data)

    def test_cam_info(self):
        response = self.client.get(url_for('Campaign_Info', Campaign_ID=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Cities of Chrey', response.data)

    def test_bo_info(self):
        response = self.client.get(url_for('Book_Info', Book_ID=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Dungeon Masters Guide', response.data)

    def test_view_new_pla(self):
        response = self.client.get(url_for('Add_Player'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Your Name', response.data)
    
    def test_view_new_cam(self):
        response = self.client.get(url_for('Add_Campaign'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Your Name', response.data)

    def test_view_new_bo(self):
        response = self.client.get(url_for('Add_Book'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The Campaign Name', response.data)

    def test_view_edit_pla(self):
        response = self.client.get(url_for('Edit_Player', Player_ID=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The Campaign Name', response.data)

    def test_view_edit_cam(self):
        response = self.client.get(url_for('Edit_Campaign', Campaign_ID=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The Books Name', response.data)

    def test_view_edit_bo(self):
        response = self.client.get(url_for('Edit_Book', Player_ID=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The Books Name', response.data)