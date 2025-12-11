from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Головна сторінка магазину"""
    return render_template('index.html', 
                         title='Головна - SportWear Україна',
                         active_page='home')

@app.route('/about')
def about():
    """Сторінка "Про нас" """
    return render_template('about.html',
                         title='Про нас - SportWear Україна',
                         active_page='about')

@app.route('/catalog')
def catalog():
    """Сторінка каталогу товарів"""
    # Мок-дані товарів (можна замінити на реальну БД)
    products = [
        {'id': 1, 'name': 'Футболка "Сила України"', 'price': 850, 'image': 'https://via.placeholder.com/300x200/005BBB/FFFFFF?text=Футболка'},
        {'id': 2, 'name': 'Кросівки "Карпати"', 'price': 2499, 'image': 'https://via.placeholder.com/300x200/FFD700/000000?text=Кросівки'},
        {'id': 3, 'name': 'Спортивний костюм', 'price': 1799, 'image': 'https://via.placeholder.com/300x200/005BBB/FFD700?text=Костюм'},
        {'id': 4, 'name': 'Кепка "Слава Україні"', 'price': 450, 'image': 'https://via.placeholder.com/300x200/FFD700/005BBB?text=Кепка'},
    ]
    return render_template('catalog.html',
                         title='Каталог - SportWear Україна',
                         active_page='catalog',
                         products=products)

@app.route('/services')
def services():
    """Сторінка послуг"""
    services_list = [
        'Безкоштовна доставка по Україні від 1500 грн',
        'Експрес-доставка по Києву (2-3 години)',
        'Повернення товару протягом 14 днів',
        'Індивідуальне нанесення принтів',
        'Консультація спортивного тренера'
    ]
    return render_template('services.html',
                         title='Послуги - SportWear Україна',
                         active_page='services',
                         services=services_list)

@app.route('/contacts')
def contacts():
    """Сторінка контактів"""
    contact_info = {
        'address': 'Київ, вул. Спортивна, 15',
        'phone': '+380 (44) 123-45-67',
        'email': 'info@sportwear.ua',
        'hours': 'Пн-Пт: 9:00-20:00, Сб-Нд: 10:00-18:00'
    }
    return render_template('contacts.html',
                         title='Контакти - SportWear Україна',
                         active_page='contacts',
                         contacts=contact_info)

if __name__ == '__main__':
    app.run(debug=True, port=5000)