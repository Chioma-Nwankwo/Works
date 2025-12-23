from flask import *
from app.menu import menu_bp
from app.menu.forms import MenuForm
from app.menu.models import Menu
from app import db


@menu_bp.route('/menu_list', methods=['GET'])
def get_menu_list(): 
    menu=Menu.query.all()
    return render_template ('menu.html', men=menu)

#GET-retrieve information and passes the info to the html page
#POST-to submit the data
#delete-delete or to remove





@menu_bp.route('/add_menu', methods=['GET', 'POST'])
def add_menu():
   forms = MenuForm()
   if forms.validate_on_submit():
      menu_name = forms.name.data
      menu_code = forms.code.data

      #insert the record
      new_menu=Menu(name= menu_name, code= menu_code)
      db.session.add(new_menu)
      db.session.commit()
      return redirect(url_for('menu.get_menu_list'))
   return render_template('add_menu.html', form=forms)
      
#method to delete a row from the website

@menu_bp.route('/delete_menu/<int:id>', methods=['POST'])
def delete_menu(id)      :
   menu=Menu.query.get_or_404(id)
   db.session.delete(menu)
   db.session.commit()
   return redirect(url_for('menu.get_menu_list'))

#method to update menu record
@menu_bp.route('/edit_menu/<int:id>', methods=['GET', 'POST'])
def update_menu(id):
   menu=Menu.query.get_or_404(id)
   forms = MenuForm(obj=menu)
   if forms.validate_on_submit():
      forms.populate_obj(menu)
      db.session.commit()
      return redirect(url_for('menu.get_menu_list'))
   return render_template('add_menu.html', form=forms)

#method to delete all row from the website

@menu_bp.route('/delete_all_menu', methods=['POST'])
def delete_all_menu():
   Menu.query.delete()
   db.session.commit()
   return redirect(url_for('menu.get_menu_list'))