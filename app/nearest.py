import sqlite3
from sqlite3 import Error
from haversine import haversine
from math import inf

def distance(my_coords, table_coords):
        return haversine(my_coords, table_coords) # en km


def selectNearest(db, table, my_lat, my_lon):
    my_coords = (my_lat, my_lon)
    selects = '''SELECT id_grp, lat_grp, lon_grp
                FROM %s''' % (table)

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

        return 'https://www.google.com/maps/place/%f,%f' % (nearest_coords[0], nearest_coords[1])

    except Error as e:
        print(e)
