from flask import *
from app.order import order_bp
from app.order.models import Order
from app.order.forms import OrderForm
from app import db

@order_bp.route('/order_list', methods=['GET'])
def get_order_list():
    order=Order.query.all() #retreiving all records from the order
    return render_template ('order.html', ord=order)

@order_bp.route('/add_order', methods=['GET', 'POST'])
def add_orders():
    forms=OrderForm()
    if forms.validate_on_submit():
        menu_id=forms.menu_id.data
        order_name=forms.name.data
        order_code=forms.code.data
       #insert the record to the relational database management 
        new_order=Order(menu_id=menu_id, name= order_name, code= order_code)
        db.session.add(new_order)
        db.session.commit()
        return redirect(url_for('order.get_order_list'))

    return render_template('add_order.html', fm=forms)

@order_bp.route('/delete_order/<int:id>', methods=['POST'])
def delete_order(id)      :
   order=Order.query.get_or_404(id)
   db.session.delete(order)
   db.session.commit()
   return redirect(url_for('order.get_order_list'))

@order_bp.route('/update_order/<int:id>',methods=['GET', 'POST'])
def update_order(id):
    order=Order.query.get_or_404(id)
    form=OrderForm(obj=order)
    if form.validate_on_submit():
        #populate the record
        form.populate_obj(order)
        db.session.commit()
        return redirect(url_for('order.get_order_list'))
    return render_template('add_order.html',fm=form)

@order_bp.route('/delete_all_orders', methods=['POST'])
def delete_all_orders():
   Order.query.delete()
   db.session.commit()
   return redirect(url_for('order.get_order_list'))
