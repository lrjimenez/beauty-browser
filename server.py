"""Server for Beauty Browser"""

from flask import (Flask, request, render_template, session, redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    product_types = crud.get_product_types()
    brands = crud.get_brands()
    return render_template('index.html', product_types=product_types, brands=brands)


@app.route('/products')
def all_products():
    all_products = crud.get_products()
    return render_template('products.html', all_products=all_products)

@app.route("/products/<product_id>")
def show_product(product_id):
    """Show details on a particular product."""

    product = crud.get_product_by_id(product_id)

    return render_template("product_details.html", product=product)

@app.route('/search-products')
def browse_by_type():
    """Show all types of products."""

    product_type_id = request.args.get('choose-type')
    brand_id = request.args.get('choose-brand')  
    print("**********product_type_id:", product_type_id, "brand_id:", brand_id)
    user_selection = crud.get_products_by_product_type_id_and_brand_id(product_type_id=product_type_id, brand_id=brand_id)
    print("*********** user_selection:", user_selection)
    
    

    return render_template('product_results.html', user_selection=user_selection)

# @app.route('/brand')
# def browse_by_brand():


#     """Query database and return all brands."""

#     sql = "SELECT product_type FROM product_types;"

#     cursor = db.session.execute(sql)
#     all_product_types = cursor.fetchall()

#     return render_template('type.html', all_product_types=all_product_types)



if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')
