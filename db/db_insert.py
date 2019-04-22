#!/usr/bin/python

def db_insert_table(cur,table,amount,transaction_type,description,user_name,balance):
  cur.execute ("INSERT INTO %s (current_balance,transaction_type,transaction_amount,user_name,description,timestamp) VALUES (%s,'%s',%s,'%s','%s',CURRENT_TIMESTAMP);" % (table,balance,transaction_type,amount,description,user_name))


