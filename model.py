"""Models for Beauty Browser app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Brand(db.Model):
    """A Brand."""

    __tablename__ = "brands"

    brand_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    company_name = db.Column(db.String)
    company_website = db.Column(db.String)

    def __repr__(self):
        return f"<Brand brand_id={self.brand_id} company_name={self.company_name}>"
    products = db.relationship('Product', back_populates = "brand")


class Product_Type(db.Model):
    """A Type of Product."""

    __tablename__ = "product_types"

    product_type_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    product_type = db.Column(db.String)

    def __repr__(self):
        return f"<Product_Type product_type_id={self.product_type_id} product_type={self.product_type}>"
    products = db.relationship('Product', back_populates = "product_type")
    

class Product(db.Model):
    """A Product."""
    
    __tablename__ = "products"

    product_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    product_name = db.Column(db.String)
    description = db.Column(db.String)
    rating = db.Column(db.String, nullable=True)
    brand_id = db.Column(db.Integer, db.ForeignKey("brands.brand_id"))
    product_type_id = db.Column(db.Integer, db.ForeignKey("product_types.product_type_id"))
    formulation_id = db.Column(db.Integer, db.ForeignKey("formulations.formulation_id"), nullable=True)
    currency_id = db.Column(db.Integer, db.ForeignKey("currencies.currency_id"))
    image_id = db.Column(db.Integer, db.ForeignKey("images.image_id"))

    def __repr__(self):
        return f"<Product product_id={self.product_id} product_name={self.product_name}>"
    brand = db.relationship('Brand', back_populates = "products")
    product_type = db.relationship('Product_Type', back_populates = "products")
    formulation = db.relationship('Formulation', back_populates = "products")
    currencies = db.relationship('Currency', back_populates = "products")
    images = db.relationship('Image', back_populates = "product")
    tags = db.relationship('Tag', back_populates = "products")
    

class Image(db.Model):
    """An Image."""

    __tablename__ = "images"

    image_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    image_link = db.Column(db.String)
    
    def __repr__(self):
        return f"<Image image_id={self.image_id} image_link={self.image_link}>"
    product = db.relationship('Product', back_populates = "images")


class Formulation(db.Model):
    """A Formulation."""

    __tablename__ = "formulations"

    formulation_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    formulation_category = db.Column(db.String)

    def __repr__(self):
        return f"<Formulation formulation_id={self.formulation_id} formulation_category={self.formulation_category}>"
    products = db.relationship('Product', back_populates = "formulation")

class Tag(db.Model):
    """A Tag."""

    __tablename__ = "tags"

    tag_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    product_tag = db.Column(db.String, nullable=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.product_id"))

    def __repr__(self):
        return f"<Tag tag_id={self.tag_id} product_tag={self.product_tag}>"
    products = db.relationship('Product', back_populates = "tags")
    

class Currency(db.Model):
    """A Currency."""

    __tablename__ = "currencies"

    currency_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    currency_type = db.Column(db.String)
    currency_sign = db.Column(db.String)

    def __repr__(self):
        return f"<Currency currency_id={self.currency_id} currency_type={self.currency_type}>"
    products = db.relationship('Product', back_populates = "currencies")


##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///beauty"
    app.config["SQLALCHEMY_ECHO"] = False
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    print("Connected to db!")



if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask

    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    connect_to_db(app)
    

    