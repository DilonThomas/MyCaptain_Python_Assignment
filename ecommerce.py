from flask import Flask, render_template, request, session, redirect, url_for
from flask_mysqldb import MySQL
import stripe

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your_mysql_password'
app.config['MYSQL_DB'] = 'your_database_name'
mysql = MySQL(app)

# Configure Stripe
stripe.api_key = 'your_stripe_secret_key'
stripe_public_key = 'your_stripe_public_key'

# Define the product data structure
products = {
    '1': {'name': 'Product 1', 'description': 'This is product 1', 'price': 10.0},
    '2': {'name': 'Product 2', 'description': 'This is product 2', 'price': 20.0},
    '3': {'name': 'Product 3', 'description': 'This is product 3', 'price': 30.0},
}

@app.route('/')
def home():
    # Display the home page
    return render_template('home.html')

@app.route('/products')
def product_list():
    # Display the list of products
    return render_template('product_list.html', products=products)

@app.route('/product/<id>')
def product_details(id):
    # Display the details of a specific product
    product = products.get(id)
    if not product:
        return redirect(url_for('product_list'))
    return render_template('product_details.html', product=product)

@app.route('/cart')
def cart():
    # Retrieve the cart information from the session
    cart = session.get('cart', {})
    cart_items = []
    total = 0
    for product_id, product in cart.items():
        subtotal = product['price'] * product['quantity']
        total += subtotal
        cart_items.append({'id': product_id, 'name': product['name'], 'price': product['price'], 'quantity': product['quantity'], 'subtotal': subtotal})
    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    # Retrieve the product information from the request
    product_id = request.form.get('id')
    quantity = int(request.form.get('quantity'))

    # Retrieve the cart information from the session
    cart = session.get('cart', {})
    cart_item = cart.get(product_id)
    if cart_item:
        cart_item['quantity'] += quantity
    else:
        product = products.get(product_id)
        if product:
            cart[product_id] = {'name': product['name'], 'price': product['price'], 'quantity': quantity}
    session['cart'] = cart

    return redirect(url_for('cart'))

@app.route('/remove_from_cart/<id>')
def remove_from_cart(id):
    # Retrieve the cart information from the session
    cart = session.get('cart', {})
    if id in cart:
        del cart[id]
        session['cart'] = cart
    return redirect(url_for('cart'))

@app.route('/checkout', methods=['POST'])
def checkout():
    # Retrieve the cart information from the session
    cart = session.get('cart', {})
    cart_items = []
    total = 0
    for product_id, product in cart.items():
        subtotal = product['price'] * product['quantity']
        total += subtotal
        cart_items.append({'id': product_id, 'name': product['name'], 'price'})
