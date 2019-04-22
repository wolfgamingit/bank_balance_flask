#!/usr/bin/python
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def db_create_test(cur,db_name):
  cur.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = '%s';" % db_name)
  exists = cur.fetchone() 
  return exists

def db_table_check(cur,table):
  cur.execute("SELECT 1 FROM pg_catalog.pg_tables where schemaname = 'public' and tablename = '%s';" % table)
  exists = cur.fetchone()
  return exists

def db_create_table(cur,table):
  print "checking " + table
  exists = db_table_check(cur,table)
  print exists
  if not exists:
    cur.execute ("CREATE TABLE IF NOT EXISTS %s (id serial PRIMARY KEY, current_balance decimal NOT NULL, transaction_type varchar, transaction_amount decimal NOT NULL, user_name varchar, description varchar, timestamp TIMESTAMP);" % table)
    cur.execute ("INSERT INTO %s (current_balance,transaction_type,transaction_amount,user_name,description,timestamp) VALUES (0,'initial',0,'NA','Initial balance',CURRENT_TIMESTAMP);" % table)

def db_seed(cur):
  print "this is just a test"
  tables = ["checking","saving","credit"]
  for table in tables:
    db_create_table(cur,table)

def db_create(con):
  cur = con.cursor()
  db_name = "bank_balance"
  exists = db_create_test(cur,db_name)
  if not exists:
    cur.execute('CREATE DATABASE %s;' % db_name)
    db_seed(cur)
  else:
    db_seed(cur)
  cur.close()


