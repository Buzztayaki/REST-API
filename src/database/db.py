import os
import bson
from flask_pymongo import MongoClient
from dotenv import load_dotenv




load_dotenv()
DB_URI = os.getenv('DB_URI')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')


def connection():
    try:

        client = MongoClient(DB_URI, username=DB_USER, password=DB_PASS, authSource=DB_NAME)
        db = client.get_database(DB_NAME)
        print('conexión con exito a {}'.format(DB_NAME))
        return db
    
    except ConnectionError as connect_error:
        raise connect_error
    
    except TimeoutError as timeout_error:
        raise timeout_error
    

