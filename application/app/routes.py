from app import app
from flask import render_template, request, redirect, url_for
from bank_balance import bank_balance
from bank_balance import money_transform
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
@login_required
def index():
  user = {'/username': 'wesley'}
  balances=bank_balance.get_balances() 
  print type(balances)
  print (balances)
  return render_template('index.html', title='Home Page', checking=str(balances[2]), saving=str(balances[1]), credit=str(balances[0]))

@app.route('/paid')
def paid():
  money_transform.transform_money("credit",102.34,"charge","Testing a charge on CC","wesley")
  money_transform.transform_money("credit",100.00,"payment","Testing a payment on CC","wesley")  

@app.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('index'))
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(username=form.username.data).first()
    if user is None or not user.check_password(form.password.data):
      flash('Invalid username or password')
      return redirect(url_for('login'))
    login_user(user, remember=form.remember_me.data)
    next_page = request.args.get('next')
    if not next_page or url_parse(next_page).netloc != '':
      next_page = url_for('index')
    return redirect(next_page)
  return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('index'))

if __name__ == '__main__':
  app.run(host='0.0.0.0')
