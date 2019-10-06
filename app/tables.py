import os
import sqlite3
from sqlite3 import Error
from app.create import createTask, insertTask

def createTables(db):
    table_con = '''CREATE TABLE Containers (
                    id_con INTEGER PRIMARY KEY,
                    nbhd_con INTEGER,
                    loc_con TEXT,
                    type_con CHAR(10),
                    condition_con INTEGER,
                    FOREIGN KEY(nbhd_con) REFERENCES Barris(id_nbhd)
                );'''

    table_fur = '''CREATE TABLE Furniture (
                    id_fur INTEGER PRIMARY KEY,
                    nbhd_fur INTEGER,
                    loc_fur TEXT,
                    start_fur DATETIME,
                    end_fur DATETIME,
                    FOREIGN KEY(nbhd_fur) REFERENCES Barris(id_nbhd)
                );'''

    table_grp = '''CREATE TABLE GreenPoints (
                    id_grp INTEGER PRIMARY KEY,
                    nbhd_grp INTEGER,
                    loc_grp TEXT,
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
    except Error as e:
        print(e)


def fillBarris(db):
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
    except Error as e:
        print(e)


def fillUsers(db):
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
    except Error as e:
        print(e)


def fillGreenPoints(db):
    f = open('grp.json', 'r')
    insert_grp = str(f.read())

    try:
        insertTask(db, insert_grp)
        db.commit()
    except Error as e:
        print(e)
