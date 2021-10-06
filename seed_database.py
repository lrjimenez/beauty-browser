import os
import json
import crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')

connect_to_db(app)
db.create_all()

with open('data/brand-covergirl.json') as f:
    makeup_data = json.loads(f.read())
