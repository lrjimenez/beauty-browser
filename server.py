"""Server for Beauty Browser"""

from flask import (Flask, request, render_template, session, redirect, jsonify)
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
    """Show products by user selection"""

    product_type_id = request.args.get('choose-type')
    company_name = request.args.get('choose-brand')  
    
    user_selection = crud.get_products_by_product_type_id_and_company_name(product_type_id=product_type_id, company_name=company_name)
    
    
    

    return render_template('product_results.html', user_selection=user_selection)

@app.route('/api/brand-list')
def get_brand_list():
    """Get brands from radio button selection"""
    product_type_id = request.args.get("productTypeId")
    brand_list = crud.get_brands_by_product_type_id(product_type_id)
    return jsonify(brand_list)

@app.route('/chart')
def show_chartjs():
    """Show chart."""

    return render_template('chart.html')

@app.route('/brand-ratings')
def get_brand_avg_rating():
    """"""
       

if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug="True", host ="0.0.0.0")
