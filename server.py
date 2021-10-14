"""Server for Beauty Browser"""

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from model import connect_to_db
import crud

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def product():
    all_products = crud.get_products()
    return render_template('products.html', all_products=all_products)

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
