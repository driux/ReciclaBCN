import os
import sqlite3
from sqlite3 import Error
from create import createDatabase
from haversine import haversine
from math import inf

def distance(my_coords, table_coords):
        return haversine(my_coords, table_coords) # en km


def selectNearest(db, my_lat, my_lon):
    my_coords = (my_lat, my_lon)
    selects = '''SELECT id_grp, lat_grp, lon_grp
                FROM GreenPoints'''

    try:
        cur = db.cursor()
        cur.execute(selects)
        results = cur.fetchall()
        nearest = float(inf)
        nearest_coords = ()

        for r in results:
            table_coords = (r[1], r[2])
            dist = distance(my_coords, table_coords)
            if dist < nearest:
                nearest = dist
                nearest_coords = table_coords

        #return 'https://www.google.com/maps/embed/place/%f,%f' % (nearest_coords[0], nearest_coords[1])
        return 'https://www.google.com/maps/embed/v1/place?q=%f,%f&amp' % (nearest_coords[0], nearest_coords[1])

    except Error as e:
        print(e)

def getNearest(lat, lon):
    return selectNearest(db, lat, lon)


if __name__ == '__main__':
    database = 'data.db'

    db = sqlite3.connect(database)

    if db is not None:
        lat, lon = 41.385063, 2.173404
        src = getNearest(lat, lon)
        print(src)

    else:
        print('No such database :(')
