from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink

from app import admin
from app.models import albums, artists, customers, db, employees


class AdminModelView(ModelView):
    """customized model view for flask-admin"""
    column_searchable_list = ['Title']
    column_filters = ['Title']
    page_size = 50

if __name__ == "__main__":

    admin.add_view(AdminModelView(albums, db.session))
    admin.add_view(ModelView(employees, db.session))
    admin.add_view(ModelView(customers, db.session))
    admin.add_view(ModelView(artists, db.session))
    admin.add_link(MenuLink(name='Home Page', url='/test', category='Links'))