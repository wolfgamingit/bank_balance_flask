#!/usr/bin/python
import bank_balance

def transform_money(account,amount,transaction_type,description,user_name):
  print "transforming the moneys"
  opposite_amount = amount * -1
  print "transform " + str(amount) + " to new amount " + str(opposite_amount)
  account_cur_bal = bank_balance.get_balance(account)
  if account == 'credit':
    if transaction_type == 'charge':
      bank_balance.set_balance('checking',opposite_amount,transaction_type,description,user_name)
      bank_balance.set_balance('saving',amount,transaction_type,description,user_name)
      bank_balance.set_balance('credit',amount,transaction_type,description,user_name)
      print "Charging to the credit card."
    elif transaction_type == 'payment':
      print "Paying the CC Bill"
      bank_balance.set_balance('saving',opposite_amount,transaction_type,description,user_name)
      bank_balance.set_balance('credit',opposite_amount,transaction_type,description,user_name)
  else:
    if transaction_type != 'deposit':
      bank_balance.set_balance(account,amount,transaction_type,description,user_name)
    else:
      bank_balance.set_balance(account,amount,transaction_type,description,user_name)

