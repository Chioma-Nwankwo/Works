from flask import *
from app.customer import customer_bp
from app.customer.models import Customer
from app.customer.forms import CustomerForm
from app import db

@customer_bp.route('/customer_list', methods=['GET'])
def get_customer_list():
    customer=Customer.query.all()
    return render_template ('customer.html', cus=customer)

@customer_bp.route('/add_customerdetails', methods=['GET', 'POST'])
def add_customerdetails():
    forms=CustomerForm()
    if forms.validate_on_submit():
        order_id=forms.order_id.data
        customer_name=forms.name.data
        customer_code=forms.code.data
        total_price=forms.price.data
        #insert the record to the relational database management 
        new_customer=Customer(order_id= order_id, name= customer_name, code= customer_code, price= total_price)
        db.session.add(new_customer)
        db.session.commit()
        return redirect(url_for('customer.get_customer_list'))

    return render_template('add_customerdetails.html', fc=forms)

@customer_bp.route('/delete_customer/<int:id>', methods=['POST'])
def delete_customer(id)      :
   customer=Customer.query.get_or_404(id)
   db.session.delete(customer)
   db.session.commit()
   return redirect(url_for('customer.get_customer_list'))

@customer_bp.route('/update_customer/<int:id>',methods=['GET', 'POST'])
def update_customer(id):
    customer=Customer.query.get_or_404(id)
    form=CustomerForm(obj=customer)
    if form.validate_on_submit():
        #populate the record
        form.populate_obj(customer)
        db.session.commit()
        return redirect(url_for('customer.get_customer_list'))
    return render_template('add_customerdetails.html',fc=form)

@customer_bp.route('/delete_all_customers', methods=['POST'])
def delete_all_customers():
   Customer.query.delete()
   db.session.commit()
   return redirect(url_for('customer.get_customer_list'))

