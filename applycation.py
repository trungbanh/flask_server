from flask import Flask
from flask import render_template
from flask import request
from pymongo import MongoClient
import json

client = MongoClient('mongodb://admin:admin@localhost:27017')
#print(client)
db = client.admin
colections = db['info']

app = Flask(__name__)
@app.route('/index')
def index ():
    return 'index'

@app.route('/login',methods=['POST'])
def login ():
    if request.method == 'POST' :
        contend = json.loads(request.get_json())
        print (contend)
    return ''
@app.route('/user/<username>')
def user (username=None):
    return render_template('hello.html',name=username)

@app.route('/add/<int:a>/<int:b>')
def add (a,b):
    result =a+b
    return str(result)

@app.route('/secret',methods=['POST'])
def secret_post ():
    if request.method == 'POST':
        contend = request.get_json()
        print(colections.find_one(contend))
        return str(colections.find_one(contend))

@app.route('/database/<name>')
def database_get (name):    
    print(colections.find_one({'name':name}))
    return str(colections.find_one({'name':name}))

@app.route('/layout')
def layout ():
    return render_template('layout.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',post=5000,debug=True)