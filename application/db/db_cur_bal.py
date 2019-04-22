#!/usr/bin/python

def db_credit_balance(cur,account):
  cur.execute("select current_balance from %s order by id DESC limit 1;" % account)
  output = cur.fetchone()
  return output
