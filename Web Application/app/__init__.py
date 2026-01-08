from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.password import *

db = SQLAlchemy()
migrate = Migrate()


DB_USER = 'root'
DB_PASSWORD = get_password()
DB_HOST = 'localhost'
DB_NAME ='restaurant_menu_order'






def create_app():
    app = Flask(__name__) 
    app.secret_key='chioma1234'


    @app.route('/') 
    def index():
        return render_template('index.html')
    
    

    DATABASE_URI=f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'

    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    
    global db
    db.init_app(app)
    migrate.init_app(app, db) 
    


    
    #registered the blueprint for the modules
    from app.home import home_bp
    app.register_blueprint(home_bp)
    from app.about import about_bp
    app.register_blueprint(about_bp)
    from app.contact import contact_bp
    app.register_blueprint(contact_bp)
    from app.menu import menu_bp
    app.register_blueprint(menu_bp)
    from app.order import order_bp
    app.register_blueprint(order_bp)
    from app.customer import customer_bp
    app.register_blueprint(customer_bp)



    #import model
    from app.menu.models import Menu
    from app.order.models import Order
    from app.about.models import About
    from app.home.models import Home
    from app.contact.models import Contact
    from app.customer.models import Customer

    #import everything
    with app.app_context():
        db.create_all()


    return app

