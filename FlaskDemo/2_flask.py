# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 22:59:20 2018

@author: SilverDoe
"""
from flask import (Flask, request, render_template)
import sqlite3 as sql

app = Flask(__name__)
conn = sql.connect('studatabase.db')
print("Opened database successfully")

conn.execute('CREATE TABLE if not exists students (uid INTEGER PRIMARY KEY AUTOINCREMENT ,name TEXT, addr TEXT, city TEXT, pin TEXT)')
print("Table created successfully")
conn.close()


@app.route('/')
def home():
   return render_template('home.html')

@app.route('/enternew')
def new_student():
   return render_template('student.html')

@app.route('/updaterec')
def update_student():
   return render_template('updatestudent.html')

@app.route('/deleterec')
def delete_rec():
   return render_template('deletestudent.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   
   if request.method == 'POST':

       try:
           nm = request.form['nm']
           addr = request.form['add']
           city = request.form['city']
           pin = request.form['pin']
         
           with sql.connect("studatabase.db") as con:
               cur = con.cursor()
            
               cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin) )
            
               con.commit()
           msg = "Record successfully added"
       except:
           con.rollback()
           msg = "error in insert operation"
      
       finally:
           return render_template("result.html",msg = msg)
           con.close()

@app.route('/editrec',methods = ['POST', 'GET'])
def updaterec():

    try:
        uid = request.form['uid']
        nm = request.form['nm']
        addr = request.form['add']
        city = request.form['city']
        pin = request.form['pin']
         
        with sql.connect("studatabase.db") as con:
            cur = con.cursor()
            
            cur.execute("UPDATE students set name ='"+nm+"', addr='"+addr+"', city='"+city+"', pin='"+pin+"' where uid="+uid)
            
            con.commit()
        msg = "Record successfully updated"
    except:
        con.rollback()
        msg = "error in update operation"
      
    finally:
        return render_template("result.html",msg = msg)
        con.close()
  
@app.route('/remrec',methods = ['POST', 'GET'])
def deleterec():
    try:
        uid = request.form['uid']
        
        with sql.connect("studatabase.db") as con:
            cur = con.cursor()
            
            cur.execute("DELETE from students where uid="+uid)
            con.commit()
        msg = "Record successfully deleted"
    except:
        con.rollback()
        msg = "error in delete operation"
    finally:
        return render_template("result.html",msg = msg)
        con.close()

@app.route('/listst')
def liststu():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from students")
   
   rows = cur.fetchall();
   return render_template("list.html",rows = rows)

if __name__ == '__main__':
   app.run(debug = False)











