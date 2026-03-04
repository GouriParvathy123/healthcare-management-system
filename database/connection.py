import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "healthcare.db")

def get_connection():
    print("Using DB:", DB_PATH)
    return sqlite3.connect(DB_PATH)