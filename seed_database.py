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
    small_set = makeup_data[0:5]
    pprint(small_set)
    
# Create brands, store them in list
brands_in_db = set()
for product in makeup_data:
    company_name, company_website = (
        product['brand'],
        product['website_link'],
    )
    #create a tuple with product brand and website link
    brand_tuple = (company_name, company_website)
    #add tuples to list of brands
    brands_in_db.add(brand_tuple)
#add the tuple to a set

print("Number of unique_brands: ", len(brands_in_db))

#for tuple in set
for brand in brands_in_db:
    db_brand = crud.create_brand(brand[0], brand[1])
   

# Create product_types, store them in list
product_types_in_db = []
for product in makeup_data:
    product_type = (
        product['product_type'],
    )
    #create a tuple with product_types
    create_tuple = [product_type]
    product_type_tuple = tuple(create_tuple)
    #add tuples to list of product_types
    product_types_in_db.append(product_type_tuple)
#add the tuple to a set
unique_product_types = set(product_types_in_db)
print("Number of unique product_types: ", len(unique_product_types))

#for tuple in set
for product_type in unique_product_types:
    db_product_type = crud.create_product_type(product_type)


# Create products, store them in list
products_in_db = []
for product in makeup_data:
    product_name, description, rating = (
        product['name'],
        product['description'],
        product['rating'],
    )
    #create a tuple with products
    create_tuple = [product_name, description, rating]
    product_tuple = tuple(create_tuple)
    #add tuple to list of products 
    products_in_db.append(product_tuple)
#add the tuple to a set
unique_products = set(products_in_db)
print("Number of unique products: ", len(unique_products))

#for tuple in set
for product in unique_products:
    db_products = crud.create_product(product[0], product[1], product[2])


# Create images, store them in list
images_in_db = []
for product in makeup_data:
    image_link = (
        product['image_link'],
    )
    #create a tuple with images_links
    create_tuple = [image_link]
    images_tuple = tuple(create_tuple)
    #add tuple to list of images
    images_in_db.append(images_tuple)
#add the tuple to a set
unique_images = set(images_in_db)
print("Number of unique images: ", len(unique_images))

#for tuple in set
for image in unique_images:
    db_images = crud.create_image(image)


# Create formulations, store them in list
formulations_in_db = set()
for product in makeup_data:
    formulation_category = product['category']
   
    formulations_in_db.add(formulation_category)

print("Number of unique formulations: ", len(formulations_in_db))

#for tuple in set
for formulation in formulations_in_db:
    print(formulation)
    db_formulations = crud.create_formulation(formulation)
