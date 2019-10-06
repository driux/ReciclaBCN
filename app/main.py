import os
import sqlite3
from create import createDatabase
from tables import createTables, fillBarris, fillUsers, fillGreenPoints

if __name__ == '__main__':
    database = 'data.db'

    db = createDatabase(os.path.abspath(database))

    if db is not None:
        createTables(db)
        fillBarris(db)
        fillUsers(db)
        fillGreenPoints(db)

    else:
        print('No such database :(')
