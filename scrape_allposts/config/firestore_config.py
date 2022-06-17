import firebase_admin
from firebase_admin import db
from firebase_admin import firestore

from scrape_allposts.pojos.SingletonMeta import SingletonMeta


class FirestoreConfig(metaclass=SingletonMeta):
    _firebase_db = None
    _firebase_ref = None
    _firestore_client = None

    def __init__(self):
        credentials_obj = firebase_admin.credentials.Certificate('./settings_firestore.json')
        firebase_admin.initialize_app(credentials_obj, {
            'databaseURL': "https://gamiblog-scraper-default-rtdb.firebaseio.com"
        })

        self.firebase_db = db
        self.firebase_ref = db.reference()
        self.firestore_client = firestore.client()

    @property
    def firebase_db(self):
        return self._firebase_db

    @firebase_db.setter
    def firebase_db(self, firebase_db):
        self._firebase_db = firebase_db

    @property
    def firebase_ref(self):
        return self._firebase_ref

    @firebase_ref.setter
    def firebase_ref(self, firebase_ref):
        self._firebase_ref = firebase_ref

    @property
    def firestore_client(self):
        return self._firestore_client

    @firestore_client.setter
    def firestore_client(self, firestore_client):
        self._firestore_client = firestore_client
