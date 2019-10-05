import sqlite3
from sqlite3 import Error
import create

def createTables(db):
    table_con = '''CREATE TABLE Containers (
                    id_con INTEGER PRIMARY KEY,
                    nbhd_con INTEGER,
                    loc_con CHAR(30),
                    type_con CHAR(10),
                    condition_con CHAR(30),
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
                    loc_fur CHAR(30),
                    lat_grp FLOAT,
                    lon_grp FLOAT,
                    start_grp DATETIME,
                    end_grp DATETIME,
                    FOREIGN KEY(nbhd_grp) REFERENCES Barris(id_nbhd)
                );'''

    table_usr = '''CREATE TABLE Users (
                    id_usr TEXT PRIMARY KEY,
                    psw_usr CHAR(20) NOT NULL,
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
                        (3, 'Sants-Monjuic'),
                        (4, 'Les Corts'),
                        (5, 'Sarria-Sant Gervsi'),
                        (6, 'Gracia'),
                        (7, 'Horta-Guinardo'),
                        (8, 'Nou Barris'),
                        (9, 'Sant Andreu'),
                        (10, 'Sant Marti');'''

    try:
        insertTask(db, insert_nbhd)
    except Error as e:
        print(e)


def createUsers(db):
    insert_usr = '''INSERT INTO Users
                        (id_usr, psw_usr, pts_usr)
                    VALUES
                        (raul@example.com, 1234abc, 100),
                        (jose@example.com, 1234abc, 150),
                        (marina@example.com, 1234abc, 320),
                        (pau@example.com, 1234abc, 250),
                        (lena@example.com, 1234abc, 100);'''

    try:
        insertTask(db, insert_usr)
    except Error as e:
        print(e)


if __name__ == '__main__':
    database = "Data/file.db"

    db = createDatabase(os.path.abspath(database))

    if db is not None:
        createTables(db)
        createBarris(db)
        createUsers(db)

    else:
        print("No such database :(")
