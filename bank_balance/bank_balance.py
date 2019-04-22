#!/usr/bin/python
import db.db_connect as DB
import db.db_create as DBCreate
import db.db_cur_bal as cur_bal
import db.db_insert as DBInsert

def get_balances():
  con = DB.db_connect()
  cur = con.cursor()
  DBCreate.db_create(con)

  output=cur_bal.db_credit_balance(cur,'credit')
  credit_val = float(output[0])
  print credit_val

  output=cur_bal.db_credit_balance(cur,'saving')
  saving_val = float(output[0])
  print saving_val

  output=cur_bal.db_credit_balance(cur,'checking')
  checking_val = float(output[0])
  print checking_val

  DB.db_disconnect(con,cur)
  return credit_val, saving_val, checking_val;

def get_balance(table):
  print "get current balance for " + table
  con = DB.db_connect()
  cur = con.cursor()

  output=cur_bal.db_credit_balance(cur,table)
  bal_val = float(output[0])
  print bal_val
  DB.db_disconnect(con,cur)
  return bal_val

def set_balance(table,amount,transaction_type,description,user_name):
  con = DB.db_connect()
  cur = con.cursor()
  print "set balances"
  cur_bal = get_balance(table)
  print "We're changing " + table + " by "+ str(amount) + " with transaction_type of " + transaction_type + " with description of " + description + " by " + user_name
  n_bal = cur_bal + amount
  print "New balance is " + str(n_bal)
  DBInsert.db_insert_table(cur,table,amount,transaction_type,description,user_name,n_bal)
  DB.db_disconnect(con,cur)

