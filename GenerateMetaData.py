import os
import glob
import mysql.connector
import json
db = mysql.connector.connect(
    host="192.168.178.10", user="root", password="pwd", database="alpha_world")
cursor = db.cursor()

path = os.path.join(os.path.dirname(__file__), 'images')

images = []

for name in glob.iglob('images/**/*.png', recursive=True):
    id = os.path.splitext(os.path.basename(name))[0]
    dir = os.path.basename(os.path.dirname(name))
    cursor.execute(
        "SELECT entry, name, subname, scale FROM creature_template WHERE (display_id1 = %s OR display_id2 = %s OR display_id3 = %s OR display_id4 = %s)", (id, id, id, id))
    result = cursor.fetchall()
    used_by = []
    color = 'success'
    for entry, name, subname, scale in result:
        used_by.append({"entry": entry, "name": name, "subname": subname or '', "scale": scale or 1.0, "not_in_alpha": entry >= 5759})
        if entry >= 5759:
            color = 'warning'
    images.append({"id": id, "path": dir, "used": len(result) > 0, "used_by": used_by, "color": color })

if len(images) > 0:
    json.dump(images, open('images.json', 'w'), indent=4)
