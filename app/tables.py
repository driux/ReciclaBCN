import os
import sqlite3
from sqlite3 import Error
from create import createDatabase, createTask, insertTask, selectTask

def createTables(db):
    table_con = '''CREATE TABLE Containers (
                    id_con INTEGER PRIMARY KEY,
                    nbhd_con INTEGER,
                    loc_con CHAR(30),
                    type_con CHAR(10),
                    condition_con INTEGER,
                    FOREIGN KEY(nbhd_con) REFERENCES Barris(id_nbhd)
                );'''

    table_fur = '''CREATE TABLE Furniture (
                    id_fur INTEGER PRIMARY KEY,
                    nbhd_fur INTEGER,
                    loc_fur CHAR(30),
                    start_fur DATETIME,
                    end_fur DATETIME,
                    FOREIGN KEY(nbhd_fur) REFERENCES Barris(id_nbhd)
                );'''

    table_grp = '''CREATE TABLE GreenPoints (
                    id_grp INTEGER PRIMARY KEY,
                    nbhd_grp INTEGER,
                    loc_grp CHAR(30),
                    lat_grp FLOAT,
                    lon_grp FLOAT,
                    FOREIGN KEY(nbhd_grp) REFERENCES Barris(id_nbhd)
                );'''

    table_usr = '''CREATE TABLE Users (
                    id_usr TEXT PRIMARY KEY,
                    psw_usr CHAR(20) NOT NULL,
                    name_usr CHAR(20) NOT NULL,
                    pts_usr INTEGER
                );'''

    table_nbhd = '''CREATE TABLE Barris (
                        id_nbhd INTEGER PRIMARY KEY,
                        name_nbhd CHAR(20)
                    );'''

    try:
        createTask(db, table_fur)
        createTask(db, table_con)
        createTask(db, table_grp)
        createTask(db, table_usr)
        createTask(db, table_nbhd)
        print('--- Tables created')
    except Error as e:
        print(e)


def createBarris(db):
    insert_nbhd = '''INSERT INTO Barris
                        (id_nbhd, name_nbhd)
                    VALUES
                        (1, 'Ciutat Vella'),
                        (2, 'Eixample'),
                        (3, 'Sants-Monjuïc'),
                        (4, 'Les Corts'),
                        (5, 'Sarrià-Sant Gervasi'),
                        (6, 'Gràcia'),
                        (7, 'Horta-Guinardó'),
                        (8, 'Nou Barris'),
                        (9, 'Sant Andreu'),
                        (10, 'Sant Martí');'''

    try:
        insertTask(db, insert_nbhd)
        db.commit()
        print('--- Table Barris created')
    except Error as e:
        print(e)


def createUsers(db):
    insert_usr = '''INSERT INTO Users
                        (id_usr, psw_usr, name_usr, pts_usr)
                    VALUES
                        ('raul@example.com', '1234abc', 'Raul', 100),
                        ('jose@example.com', '1234abc', 'Jose', 150),
                        ('marina@example.com', '1234abc', 'Marina', 320),
                        ('pau@example.com', '1234abc', 'Pau', 250),
                        ('lena@example.com', '1234abc', 'Lena', 100);'''

    try:
        insertTask(db, insert_usr)
        db.commit()
        print('--- Table Users created')
    except Error as e:
        print(e)


if __name__ == '__main__':
    database = 'data.db'

    db = createDatabase(os.path.abspath(database))

    if db is not None:
        print('--- CREA')
        createTables(db)
        createBarris(db)
        createUsers(db)

    else:
        print('No such database :(')
