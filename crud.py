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

def get_product_types():
    """Return all product_types.""" 
    
    return Product_Type.query.all()

def get_brands():
    """Return all brands."""

    return Brand.query.all()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)