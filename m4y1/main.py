from flask import Flask, render_template, request
from datetime import datetime, timedelta
from random import randint


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    product = [{'name': 'Супер крутой товар',
                 'description': 'Это супер крутой товар, скорее покупай', 
                 'price':50, 
                 'img':'/static/images/2.jpg'},
                 {'name': "test",
                 'description': 'sth',
                 'price': 100,
                 'img':"/static/images/1.jpg'"}]
    return render_template('products.html', product=product)

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/product1')
def product1():
    date = datetime.strptime('2022.12.25', '%Y.%m.%d')
    delta = date - datetime.now()
    days_before_end = delta.days
    end_date = datetime.now() + timedelta(days=14)
    end_date = end_date.strftime('%d.%m.%Y')
    return render_template('product1.html', action_name='Весенние скидки', end_date=end_date, days_before_end=days_before_end, number=10)

@app.route('/product2')
def product2():
    return render_template('product2.html')

@app.route('/lootbox')
def lootbox():
    num = randint(1, 100)
    if num < 50:
        chance = 50
    elif 50 < num < 95:
        chance = 45
    elif 95 < num < 99:
        chance = 4
    else:
        chance = 1
    return render_template('lootbox.html', chance=chance)

@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        for key in request.form:
            print(key, request.form[key])
            if request.form[key] == '':
                return render_template('order.html', error='Не все поля заполнены!')
    return render_template('order.html')

@app.route('/order_list')
def order_list():
    return render_template('order_list.html')
    
if __name__ == "__main__":
    app.run()
