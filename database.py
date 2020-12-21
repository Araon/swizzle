import sqlite3
import logging
import json
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


try:
    conn = sqlite3.connect('profile.db')
except Exception as e:
    logger.error("Error Connecting to Database", exc_info=True)
    raise e
    
c = conn.cursor()


def create_schema():
    c.execute("""CREATE TABLE IF NOT EXISTS profile (
            ID INTEGER PRIMARY KEY,
            username TEXT,
            email TEXT NOT NULL UNIQUE,
            password TEXT
            )""")
    conn.commit()
    logger.info("Database Created!")


def insert_data(username,pwd,email):
    try:     
        conn = sqlite3.connect('profile.db')
    except Exception as e:
        logger.error("Error Connecting to Database", exc_info=True)
        raise e
    c = conn.cursor()
    try:
        c.execute("INSERT INTO profile (username,password,email) VALUES (?,?,?)", (username,pwd,email))
        conn.commit()
        logger.info("Database Updated, New issue inserted!")
    except sqlite3.IntegrityError:
        pass
        logger.info("Dublicate Data, not inserted")


# def isprofilethere(username,pwd):
#     try:
#         c.execute("SELECT * FROM profile WHERE ")