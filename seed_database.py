import os
import json
import crud
import model
import server

os.system('dropdb beauty')
os.system('createdb beauty')

model.connect_to_db(server.app)
model.db.create_all()

# Load makeup data from JSON file
with open('data/products.json') as f:
    makeup_data = json.loads(f.read())

    print(len(makeup_data))
# Create brands, store them in list
brands_in_db = {}
for product in makeup_data:
    company_name, company_website = (
        product['brand'],
        product['website_link'],
    )
    brands_in_db[company_name] = company_website
print("these are brands in db: ", brands_in_db)
print(len(brands_in_db))

#create a dictionary with product brand and website link
#print(brandbook)
#add the tuple to a set
#for tuple in set
    
db_brand = crud.create_brand(company_name, company_website)
#brands_in_db.append(db_brand)
#print(brands_in_db)
