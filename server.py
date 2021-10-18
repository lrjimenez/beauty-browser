"""Server for Beauty Browser"""

from flask import (Flask, request, render_template, session, redirect)
from flask_sqlalchemy import SQLAlchemy
from model import connect_to_db
import crud

from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def all_products():
    all_products = crud.get_products()
    return render_template('products.html', all_products=all_products)

@app.route("/products/<product_id>")
def show_product(product_id):
    """Show details on a particular product."""

    product = crud.get_product_by_id(product_id)

    return render_template("product_details.html", product=product)

# @app.route('/type')
# def browse_by_type():


#     """Query database and return all types of products."""

#     sql = "SELECT product_type FROM product_types;"

#     cursor = db.session.execute(sql)
#     all_product_types = cursor.fetchall()

#     return render_template('type.html', all_product_types=all_product_types)

# @app.route('/lip_liner')
# def browse_by_type():


#     """Query database and return all lipliners."""

#     sql = "SELECT product_type FROM product_types;"

#     cursor = db.session.execute(sql)
#     all_product_types = cursor.fetchall()

#     return render_template('type.html', all_product_types=all_product_types)



if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')
