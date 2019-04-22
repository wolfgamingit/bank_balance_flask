#!/usr/bin/python
from bank_balance import bank_balance
from bank_balance import money_transform

balances=bank_balance.get_balances()
#print type(balances)
#print (balances)

#bank_balance.set_balance("checking",1024,"test","This is a test transaction","wesley")
#bank_balance.set_balance("checking",-24,"test","This is a test transaction","wesley")
money_transform.transform_money("credit",102.34,"charge","Testing a charge on CC","wesley")
money_transform.transform_money("credit",100.00,"payment","Testing a payment on CC","wesley")

