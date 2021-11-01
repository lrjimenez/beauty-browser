"""CRUD operations."""

from model import db, Brand, Product_Type, Product, Image, Formulation, Tag, Currency, connect_to_db


def create_brand(company_name, company_website):
    """Create and return a brand"""

    brand = Brand(company_name=company_name, company_website=company_website)

    db.session.add(brand)
    db.session.commit()

    return brand

def create_product_type(product_type):
    """Create and return a product_type"""

    product_type = Product_Type(product_type=product_type)

    db.session.add(product_type)
    db.session.commit()

    return product_type

def create_product(product_name, description, rating, brand_id, product_type_id, currency_id, formulation_id):
    """Create and return a product."""

    product = Product(product_name=product_name, description=description, rating=rating, brand_id=brand_id, product_type_id=product_type_id, currency_id=currency_id, formulation_id=formulation_id)

    db.session.add(product)
    db.session.commit()

    return product


def create_image(image_link):
    """Create and return an image."""

    image = Image(image_link=image_link)

    db.session.add(image)
    db.session.commit()

    return image


def create_formulation(formulation_category):
    """Create and return a formulation."""

    formulation = Formulation(formulation_category=formulation_category)

    db.session.add(formulation)
    db.session.commit()

    return formulation


def create_tag(product_tag):
    """Create and return a tag."""

    tag = Tag(product_tag=product_tag)

    db.session.add(tag)
    db.session.commit()

    return tag


def create_currency(currency_type, currency_sign):
    """Create a type of currency."""

    currency = Currency(currency_type=currency_type, currency_sign=currency_sign)

    db.session.add(currency)
    db.session.commit()

    return currency

def get_products():
    """Return all products."""
    return Product.query.all()

def get_product_by_id(product_id):
    """Return one product"""
    
    return Product.query.get(product_id)

def get_product_by_product_type_id(product_type_id):
    """Return all products of one product_type_id"""

    return Product.query.filter(Product.product_type_id==(product_type_id)).all()

def get_product_types():
    """Return all product_types.""" 
    
    return Product_Type.query.all()

def get_products_by_type(type_choice):
    "Return products of the same type"
    return Product_Type.query.filter(Product_Type.product_type==(type_choice))

def get_brands():
    """Return all brands."""

    return Brand.query.all()

def get_brands_by_product_type_id(product_type_id):
    """Return brands that have at least one product of a product_type_id"""
    unique_brands = set()
    #db.session.query(Brand).join(Product).filter(Product.product_type_id==4).all()
    for product in get_product_by_product_type_id(product_type_id):
        if product.brand.company_name is not None:
            unique_brands.add(product.brand.company_name)
    return list(unique_brands)


def get_products_by_product_type_id_and_company_name(product_type_id, company_name):
    """Get products by product_type_id & company_name"""

    all_prods_of_type = Product.query.filter(Product.product_type_id == product_type_id).options(db.joinedload("brand")).all()
    prods_of_brand = []
    for prod in all_prods_of_type:
        if prod.brand.company_name == company_name:
            prods_of_brand.append(prod)
    return prods_of_brand
    # return Product.query.filter(Product.product_type_id == product_type_id, Brand.company_name == company_name).all()
    # db.session.query(Product.product_name, Brand.company_name).filter(Brand.company_name == "essie", Product.product_type_id == 3).all()

def get_avg_brand_rating(brand_id):
    """Get the average of product ratings for all products by a brand"""
    brand_ratings = db.session.query(Product.brand_id, Brand.company_name,qProduct.product_name, Product.rating).filter(Brand.brand_id == brand_id).all()




if __name__ == '__main__':
    from server import app
    connect_to_db(app)