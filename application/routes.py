from app import app
from bank_balance import bank_balance
from bank_balance import money_transform

@app.route('/')
@app.route('/index')
def index():
  balances=bank_balance.get_balances() 
  print type(balances)
  print (balances)
  return balances

@app.route('/paid')
def paid():
  money_transform.transform_money("credit",102.34,"charge","Testing a charge on CC","wesley")
  money_transform.transform_money("credit",100.00,"payment","Testing a payment on CC","wesley")  
