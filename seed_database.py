import os
import json
import crud
import model
import server
from pprint import pprint

os.system('dropdb beauty')
os.system('createdb beauty')

model.connect_to_db(server.app)
model.db.create_all()

# Load makeup data from JSON file
with open('data/products.json') as f:
    makeup_data = json.loads(f.read())
    #small_set = makeup_data[0:5]
    #pprint(small_set)
    
# Create brands, store them in a set
brands_in_db = set()
for product in makeup_data:
    company_name, company_website = (
        product['brand'],
        product['website_link'],
    )
    #create a tuple with product brand and website link
    brand_tuple = (company_name, company_website)
    #add tuples to set of brands
    brands_in_db.add(brand_tuple)

print("Number of unique_brands: ", len(brands_in_db))
#for tuple in set
for brand in brands_in_db:
    db_brand = crud.create_brand(brand[0], brand[1])
   

# Create product_types, store them in a set
product_types_in_db = set()
for product in makeup_data:
    product_type = (
        product['product_type'],
    )
    #add each type to set of product_types
    product_types_in_db.add(product_type)
print("Number of unique product_types: ", len(product_types_in_db))

for product_type in product_types_in_db:
    db_product_type = crud.create_product_type(product_type)


# Create products, store them in a set
products_in_db = set()
for product in makeup_data:
    product_name, description, rating = (
        product['name'],
        product['description'],
        product['rating'],
    )
    #create a tuple with products
    product_tuple = (product_name, description, rating)
    #add tuple to set of products
    products_in_db.add(product_tuple)

print("Number of unique products: ", len(products_in_db))

#for tuple in set
for product in products_in_db:
    db_product = crud.create_product(product[0], product[1], product[2])


# Create images, store them in list
images_in_db = set()
for product in makeup_data:
    image_link = (product['image_link'],)
    #add link to set of images
    images_in_db.add(image_link)

print("Number of unique images: ", len(images_in_db))

#for image link in set
for image in images_in_db:
    db_image = crud.create_image(image)


# Create formulations, store them in a set
formulations_in_db = set()
for product in makeup_data:
    formulation_category = product['category']
   
    formulations_in_db.add(formulation_category)

print("Number of unique formulations: ", len(formulations_in_db))

#for formulation in set
for formulation in formulations_in_db:
    #print(formulation)
    db_formulation = crud.create_formulation(formulation)

# # Create tags, store them in a set
tags_in_db = set()
for product in makeup_data:
    product_tags = product['tag_list']
    for item in product_tags:
        tags_in_db.add(item)

print("Number of unique tags: ", len(tags_in_db))

 #for tag in set
for tag in tags_in_db:
    #print(tag)
    db_tag = crud.create_tag(tag)

# Create currencies, store them in a set
currencies_in_db = set()
for product in makeup_data:
    currency_type, currency_sign = (
        product['currency'],
        product['price_sign'],
    )
    #create a tuple with currency type and sign
    currency_tuple = (currency_type, currency_sign)
    #add tuples to set of brands
    currencies_in_db.add(currency_tuple)

print("Number of currencies: ", len(currencies_in_db))
#for tuple in set
for currency in currencies_in_db:
    db_brand = crud.create_currency(currency[0], currency[1])