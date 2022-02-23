#!/usr/bin/env python
# -*- coding: utf-8 -*-
  
from flask import Flask
from pypassword import *
import pymysql
  
app = Flask(__name__)
  
class Database:
    def __init__(self):
        self.con = pymysql.connect(host=dbhost, user=dbuser, password=dbpassword, db=dbname, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()
  
    def get_content(self):
        self.cur.execute("SELECT helloworld FROM content LIMIT 50")
        result = self.cur.fetchall()
  
        return result
  
    def get_health(self):
        self.cur.execute("SELECT health_check FROM health LIMIT 1")
        result = self.cur.fetchall()
  
        return result
  
@app.route('/health')
def healthcheck():
  
    def db_query():
        db = Database()
        healthstatus = db.get_health()
  
        return healthstatus
  
    return db_query()[0].itervalues().next()
  
@app.route("/")
def hello():
    def db_query():
        db = Database()
        content = db.get_content()
  
        return content
  
    return db_query()[0].itervalues().next()
  
if __name__ == "__main__":
    app.run(host='0.0.0.0')