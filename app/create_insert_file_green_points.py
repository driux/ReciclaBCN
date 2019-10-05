import json

BARRIS = {
'Ciutat Vella' : 1,
'Eixample' : 2,
'Sants-Montjuïc' : 3,
'Les Corts' : 4,
'Sarrià-Sant Gervasi' : 5,
'Gràcia' : 6,
'Horta-Guinardó' : 7,
'Nou Barris' : 8,
'Sant Andreu' : 9,
'Sant Martí' : 10 }

f = open("file_create_green_points.py", "w")
f.write(" '''INSERT INTO GreenPoints \n (id_grp, nbhd_grp, loc_grp, lat_grp, lon_grp) \n VALUES \n ")
f.close()
with open("../green_points.json", "r") as read_file:
    data = json.load(read_file)
    f = open("file_create_green_points.py", "a")
    for i in range (0, 126):
        f.write("( " + str(i) + ", " + str(BARRIS.get(data['district'][str(i)])) + ", " + "'" + data['address'][str(i)] + "'" + ", " + str(data['gmapx'][str(i)]) + ", " + str(data['gmapy'][str(i)]) + ") \n")
    f.write("'''")
    f.close()
