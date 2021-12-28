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
    #small_set = makeup_data[0:1]
    #pprint(small_set)
    
# Create brands, store them in a set
brands_in_db = set()
for product in makeup_data:
    company_name, company_website = (
        product['brand'],
        product['website_link'],
    )
    
    brand_tuple = (company_name, company_website) #create a tuple with product brand as company_name and website link
    brands_in_db.add(brand_tuple) #add tuples to set of brands

print("Number of unique_brands: ", len(brands_in_db))
brands_dict = {} #dictionary with company name keys and brand id values

#for tuple in set
for brand in brands_in_db:
    db_brand = crud.create_brand(brand[0], brand[1]) #created a brand object of the Brand class using crud function
    brands_dict[db_brand.company_name] = db_brand.brand_id #adding to dictionary
   
# Create product_types, store them in a set
product_types_in_db = set()
for product in makeup_data:
    product_type = product['product_type']
    
    #add each type to set of product_types
    product_types_in_db.add(product_type)
print("Number of unique product_types: ", len(product_types_in_db))
product_type_ids = {} #dictionary with product type and product type id values

for every_type in product_types_in_db:
    db_product_type = crud.create_product_type(every_type)
    product_type_ids[db_product_type.product_type]=db_product_type.product_type_id

#product type id is going to be used for the products table
print("*********************")
print("*********************")
print('product_type_ids', product_type_ids)
print("*********************")
print("*********************")

# Create currencies, store them in a set
currencies_in_db = set()
for product in makeup_data:
    currency_type, currency_sign = (
        product['currency'],
        product['price_sign'],
    )
    #create a tuple with currency type and sign
    currency_tuple = (currency_type, currency_sign)
    currencies_in_db.add(currency_tuple) #add tuples to set of brands
print("Number of currencies: ", len(currencies_in_db))

currency_ids = {}
#for tuple in set
for currency in currencies_in_db:
    db_currency = crud.create_currency(currency[0], currency[1])
    currency_ids[db_currency.currency_type] = db_currency.currency_id

# Create formulations, store them in a set
formulations_in_db = set()
for product in makeup_data:
    formulation_category = product['category']
   
    formulations_in_db.add(formulation_category)

print("Number of unique formulations: ", len(formulations_in_db))
formulation_ids = {}
#for formulation in set
for formulation in formulations_in_db:
    db_formulation = crud.create_formulation(formulation)
    formulation_ids[db_formulation.formulation_category] = db_formulation.formulation_id


# Create products, store them in a set
products_in_db = set()
for product in makeup_data:
    product_name, description, rating, company_name, product_type, currency_type, formulation_category = (
        product['name'],
        product['description'],
        product['rating'],
        product['brand'],
        product['product_type'],
        product['currency'],
        product['category']
    )
    
    product_tuple = (product_name, description, rating, company_name, product_type, currency_type, formulation_category) #create a tuple with products
    products_in_db.add(product_tuple) #add tuple to set of products

print("Number of unique products: ", len(products_in_db))

#for tuple in set
for product in products_in_db:
    company_name = product[3]
    brand_id = brands_dict[company_name] #brand_id, value from the brands_dict using the company name as the key
    product_type_id = product_type_ids[product[4]]
    currency_id = currency_ids[product[5]]
    formulation_id = formulation_ids[product[6]]
    db_product = crud.create_product(product[0], product[1], product[2], brand_id, product_type_id, currency_id, formulation_id)


# Create images, store them in set
images_in_db = set()
for product in makeup_data:
    product_name, description, rating, company_name, product_type, currency_type, formulation_category = (
        product['name'],
        product['description'],
        product['rating'],
        product['brand'],
        product['product_type'],
        product['currency'],
        product['category']
    )
    brand_id = brands_dict[company_name]
    product_type_id = product_type_ids[product_type]
    currency_id = currency_ids[currency_type]
    formulation_id = formulation_ids[formulation_category]
    product_id = model.Product.query.filter(
        model.Product.product_name==product_name, 
        model.Product.description==description, 
        model.Product.brand_id==brand_id,
        model.Product.product_type_id==product_type_id,
        model.Product.currency_id==currency_id,
        model.Product.formulation_id==formulation_id,
        #model.Product.rating==string(rating),
        ).one().product_id
    image = (product['image_link'], product_id)
    images_in_db.add(image) #add link to set of images

print("Number of unique images: ", len(images_in_db))

#for image link in set
for image in images_in_db:
    db_image = crud.create_image(image[0], image[1])




# # Create tags, store them in a set
tags_in_db = set()
for product in makeup_data:
    product_tags = product['tag_list']
    for item in product_tags:
        tags_in_db.add(item)

print("Number of unique tags: ", len(tags_in_db))

 #for tag in set
for tag in tags_in_db:
    db_tag = crud.create_tag(tag)

