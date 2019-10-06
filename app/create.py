import os
import sqlite3
from sqlite3 import Error

def createDatabase(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
        print('--- Database created')
    except Error as e:
        print(e)

    return connection
    '''finally:
        if connection:
            connection.close()'''


def createTask(db, create_line):
    try:
        cur = db.cursor()
        cur.execute(create_line)
    except Error as e:
        print(e)


def insertTask(db, insert_line):
    try:
        cur = db.cursor()
        cur.execute(insert_line)
    except Error as e:
        print(e)
