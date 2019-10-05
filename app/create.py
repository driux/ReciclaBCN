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


def createTables(db):
    # Define tables
    table_fur = '''CREATE TABLE Furniture (
                    id_fur INTEGER PRIMARY KEY,
                    nbhd_fur INTEGER,
                    loc_fur CHAR(30),
                    start_fur DATETIME,
                    end_fur DATETIME,
                    FOREIGN KEY(nbhd_fur) REFERENCES Barris(id_nbhd)
                );'''

    table_con = '''CREATE TABLE Containers (
                    id_con INTEGER PRIMARY KEY,
                    nbhd_con INTEGER,
                    loc_con CHAR(30),
                    type_con CHAR(10),
                    condition_con CHAR(30),
                    FOREIGN KEY(nbhd_con) REFERENCES Barris(id_nbhd)
                    );'''

    table_grp = '''CREATE TABLE GreenPoints (
                    id_grp INTEGER PRIMARY KEY,
                    nbhd_grp INTEGER,
                    loc_grp CHAR(30),
                    start_grp DATETIME,
                    end_grp DATETIME,
                    FOREIGN KEY(nbhd_grp) REFERENCES Barris(id_nbhd)
                    );'''

    table_usr = '''CREATE TABLE Users (
                    id_usr INTEGER PRIMARY KEY,
                    pts_usr INTEGER
                    )'''

    try:
        createTask(db, table_fur)
        createTask(db, table_con)
        createTask(db, table_grp)
        createTask(db, table_usr)
        print('--- Tables created')
    except Error as e:
        print(e)


def createBarris(db):
    table_nbhd = '''CREATE TABLE Barris (
                    id_nbhd INTEGER PRIMARY KEY,
                    name_nbhd CHAR(20)
                    )'''

    insert_nbhd = '''INSERT INTO Barris
                        (id_nbhd, name_nbhd)
                    VALUES
                        (1, 'Ciutat Vella'),
                        (2, 'Eixample'),
                        (3, 'Sants-Montjuïc'),
                        (4, 'Les Corts'),
                        (5, 'Sarrià-Sant Gervasi'),
                        (6, 'Gràcia'),
                        (7, 'Horta-Guinardó'),
                        (8, 'Nou Barris'),
                        (9, 'Sant Andreu'),
                        (10, 'Sant Martí');'''

    try:
        cur = db.cursor()
        cur.execute(table_nbhd)
        cur.execute(insert_nbhd)
    except Error as e:
        print(e)


if __name__ == '__main__':
    database = "Data/file.db"

    db = createDatabase(os.path.abspath(database))

    if db is not None:
        createTables(db)
        createBarris(db)

    else:
        print("No such database :(")
