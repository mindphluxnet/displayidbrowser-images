import os
import glob
import mysql.connector
import json
db = mysql.connector.connect(
    host="localhost", user="root", password="pwd", database="alpha_world")
cursor = db.cursor()

path = os.path.join(os.path.dirname(__file__), 'images')

images = []

for name in glob.iglob('images/**/*.png', recursive=True):
    id = os.path.splitext(os.path.basename(name))[0]
    dir = os.path.basename(os.path.dirname(name))
    cursor.execute(
        "SELECT entry FROM creature_template WHERE (display_id1 = %s OR display_id2 = %s OR display_id3 = %s OR display_id4 = %s)", (id, id, id, id))
    result = cursor.fetchall()
    images.append({"id": id, "path": dir, "used": len(result) > 0})

if len(images) > 0:
    json.dump(images, open('images.json', 'w'), indent=4)
