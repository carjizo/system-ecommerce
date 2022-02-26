from flask import render_template, session, request, redirect,url_for,flash
from shop import app,db,bcrypt
# from .forms import RegistrationForm,LoginForm
# from .models import User
from shop.seller.models import User
from shop.seller.forms import RegistrationForm

@app.route('/admin')
def admin():
    users = User.query.all()
    return render_template('admin/index.html', title='seller page',users=users)

# @app.route('/brands')
# def brands():
#     brands = Brand.query.order_by(Brand.id.desc()).all()
#     return render_template('seller/brand.html', title='brands',brands=brands)


# @app.route('/categories')
# def categories():
#     categories = Category.query.order_by(Category.id.desc()).all()
#     return render_template('seller/brand.html', title='categories',categories=categories)


# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         hash_password = bcrypt.generate_password_hash(form.password.data)
#         user = User(name=form.name.data,username=form.username.data, email=form.email.data,
#                     password=hash_password)
#         db.session.add(user)
#         flash(f'welcome {form.name.data} Thanks for registering','success')
#         db.session.commit()
#         return redirect(url_for('login'))
#     return render_template('seller/register.html',title='Register user', form=form)


# @app.route('/admin/login', methods=['GET','POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         if user and bcrypt.check_password_hash(user.password, form.password.data):
#             session['email'] = form.email.data
#             flash(f'welcome {form.email.data} you are logedin now','success')
#             return redirect(url_for('seller'))
#         else:
#             flash(f'Wrong email and password', 'success')
#             return redirect(url_for('login'))
#     return render_template('seller/login.html',title='Login page',form=form)

@app.route('/updateseller/<int:id>', methods=['GET','POST'])
def updatepseller(id):
    form = RegistrationForm(request.form)
    users = User.query.get_or_404(id)
    if request.method =="POST":
        users.name = form.name.data
        users.username = form.username.data 
        users.email = form.email.data

        flash('The seller was updated','success')
        db.session.commit()
        return redirect(url_for('admin'))
    form.name.data = users.name
    form.username.data = users.username
    form.email.data = users.email

    return render_template('seller/register.html', form=form, title='Update Seller')