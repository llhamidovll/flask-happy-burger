
from flask import url_for
from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your-secret-key'

# Database Connection
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Create Database Tables
def create_tables():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            meal TEXT NOT NULL
        )
    ''')
    conn.execute('''CREATE TABLE IF NOT EXISTS payments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        payment_method TEXT NOT NULL,
        FOREIGN KEY (username) REFERENCES users (username)
    )''')


    conn.commit()
    cur.close()
    conn.close()

# Initialize Database Tables
create_tables()

# Home Page
@app.route('/')
def home():
    return render_template('home.html')

# User Registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = cur.fetchone()

        if user:
            error = 'Username already exists. Please choose a different username.'
            return render_template('register.html', error=error)

        cur.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()

        cur.close()
        conn.close()

        return redirect('/login')

    return render_template('register.html')

# User Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = cur.fetchone()

        cur.close()
        conn.close()

        if user:
            session['username'] = username
            return redirect('/order')
        else:
            error = 'Invalid username or password. Please try again.'
            return render_template('login.html', error=error)

    return render_template('login.html')

# User Logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

# User Order
@app.route('/order', methods=['GET', 'POST'])
def order():
    if 'username' not in session:
        return redirect('/login')

    meal_options = [
        {'name': 'Hamburger', 'image': 'im1.jpg'},
        {'name': 'Frensh Fries', 'image': 'im2.jpg'},
        {'name': 'Fried Chicken', 'image': 'im3.jpg'},
        {'name': 'Corn & Green Chili Salad', 'image': 'im4.jpg'},
        {'name': 'Potato Salad', 'image': 'im5.jpg'},
        {'name': 'Perfect Summer Fruit Salad', 'image': 'im6.jpg'}
    ]

    if request.method == 'POST':
        meal = request.form['meal']
        username = session['username']

        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute('INSERT INTO orders (username, meal) VALUES (?, ?)', (username, meal))
        conn.commit()

        cur.close()
        conn.close()

        return redirect('/order_history')

    return render_template('order.html', username=session['username'], meal_options=meal_options)

# User Order History
@app.route('/order_history')
def order_history():
    if 'username' not in session:
        return redirect('/login')

    username = session['username']

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute('SELECT * FROM orders WHERE username = ?', (username,))
    orders = cur.fetchall()

    cur.close()
    conn.close()

    return render_template('order_history.html', username=username, orders=orders)

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    if 'username' not in session:
        return redirect('/login')

    if request.method == 'POST':
        payment_method = request.form['payment_method']
        username = session['username']

        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute('INSERT INTO payments (username, payment_method) VALUES (?, ?)', (username, payment_method))
        conn.commit()

        cur.close()
        conn.close()

    return render_template('payment.html', username=session['username'])

@app.route('/update_payment', methods=['GET', 'POST'])
def update_payment():
    if 'username' not in session:
        return redirect('/login')

    if request.method == 'POST':
        payment_method = request.form['payment_method']
        username = session['username']

        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute('UPDATE payments SET payment_method = ? WHERE username = ?', (payment_method, username))
        conn.commit()

        cur.close()
        conn.close()

    return redirect('/payment')


if __name__ == '__main__':
    app.run(debug=True)
