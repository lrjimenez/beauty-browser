"""Server for Beauty Browser"""

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/type')
def browse_by_type():


    """Query database and return all types of products."""

    sql = "SELECT product_type FROM product_types;"

    cursor = db.session.execute(sql)
    all_product_types = cursor.fetchall()

    return render_template('type.html', all_product_types=all_product_types)
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


if __name__ == '__main__':
    connect_to_db(app)
    db.create_all()
    app.run(debug=True, host='0.0.0.0')
