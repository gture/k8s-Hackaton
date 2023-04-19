import os
from flask import Flask, request, redirect, url_for
import mysql.connector



server = Flask(__name__)
conn = None


config = {
    'host': 'mariadb-service',
    'port': 6000,
    'user': 'root',
    'password': 'secret',
    'database': 'example'
}


@server.route('/')
def testConnection():
    global conn
    if not conn:
        conn = mysql.connector.connect(**config)
        # create a connection cursor
        cur = conn.cursor()
    else:
        cur = conn.cursor()
    
    cur.execute("SELECT * FROM factorized")
    rec = cur.fetchall()
    response = ''
    for item in rec:
         product=str(item[1])
         factors=''
         for i in range(2,len(item)):
             factors=factors + '*' + str(item[i])
         response=response + '<div>   Factorization of  ' + str(product) + ' is ' + str(factors) + '</div>'

    return response
"""
    response = ''
    for c in rec:
        response = response  + '<div>   Hello  ' + c + '</div>'
"""
     

"""
@server.route('/')
def index():
    return '<div> Hello World </div>'
"""

@server.route('/factorize/<product>')
def factorize(product):
    i=2
    product=int(product)
    n=product
    factors=''
    while i < product/2:
       if n%i == 0:
           factors = factors + str(i) + '*'
           n=n/i
       else:
              i=i+1
    factors=factors[:len(factors)-1]
    
    global conn
    if not conn:
        conn = mysql.connector.connect(**config)
        # create a connection cursor
        cur = conn.cursor()
    else:
        cur = conn.cursor()
    
    cur.execute("CREATE TABLE IF NOT EXISTS factorized (id int NOT NULL AUTO_INCREMENT, product INT,factors VARCHAR(1000), PRIMARY KEY (id))")
    cur.execute("INSERT factorized (product, factors) VALUES (%s,%s)", (product, factors))
    cur.execute("SELECT (product) FROM factorized")
    rec = cur.fetchall()
#    return rec[0][0]

    return ' asdasdsad %s = %s'  %( product, factors)

@server.route('/insert',methods = ['POST', 'GET'])
def insert():
   if request.method == 'POST':
      prod = request.form['prod']
      return redirect(url_for('factorize',product=prod))
   else:
      prod = request.args.get('product')
      return redirect(url_for('success'))


if __name__ == '__main__':
    server.run(debug=True)


