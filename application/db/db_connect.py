#!/usr/bin/python
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def db_connect():
  db_name = "bank_balance"
  db_user = "user"
  db_pass = "2htLeuFhFWg5"
  db_server = "localhost"
  con = psycopg2.connect(dbname=db_name, user=db_user, host=db_server,password=db_pass)
  con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
  return con

def db_disconnect(con,cur):
  cur.close()
  con.close()


