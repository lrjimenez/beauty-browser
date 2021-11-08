# Beauty Browser
Beauty Browser displays information about cosmetic products across brands and retailers.

## Stack
Python, PostgreSQL, Flask, Jinja, HTML, CSS, Javascript

## Features
- Users can search for products by selecting a combination of product type and brand name.
- Users can view a list of all products in the database.
- Users can click out to the retail site to purchase a product. 

## How to Run
1. Set up the virtual environment  
    `virtualenv env`
2. Activate the virtual environment  
    `source env/bin/activate`
3. Install the requirements  
    `pip3 install -r requirements.txt`
4. Create the database and add data    
    `python3 seed_database.py`
5. Run the server  
    `python3 server.py`
6. View Beauty Browser at your local host   
    `http://localhost:5000/`

