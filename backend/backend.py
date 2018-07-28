import sqlite3
from hashlib import *
from flask import Flask, render_template, jsonify
from flask_cors import CORS, cross_origin

conn = sqlite3.connect('login.db')
c = conn.cursor()

def setup_stuff():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret!'

    # Enable cors (so the development server can access Python back-end (since it has different port number)
    # cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    cors = CORS(app, resources={r"/*": {"origins": "*"}})

    @app.route("/")
    def hello():
        return render_template('<h1>Hi There</h1>')

    @app.route('/ping', methods=['GET'])
    def ping_pong():
        return jsonify('pong!')

    @app.route('/pinger', methods=['POST'])
    def ping_ponger():
        return jsonify("Gottem")

    if __name__ == '__main__':
        #socketio.run(app)
        # app.run(host='0.0.0.0', port=5000)
        app.run()
#setup_stuff()

def create_table(tablename):
    c.execute("CREATE TABLE IF NOT EXISTS "+tablename+"(user TEXT,password TEXT)")

def create_table2(tablename):
    c.execute("CREATE TABLE IF NOT EXISTS "+tablename+" (user TEXT, appliance TEXT)")
def create_table3(tablename):
    c.execute("CREATE TABLE IF NOT EXISTS "+tablename+" (user TEXT, review TEXT, stars INT,upvotes INT)")

def data_entry_login(username,password):
    isInLogin=False
    c.execute("SELECT user FROM login")
    for row in c.fetchall():
        if row[0]==username:
            isInLogin=True
            break
    if isInLogin==False:
        password=encrypt(password)
        c.execute("INSERT INTO login (user,password) VALUES(?,?)",(username,password))
        conn.commit()
    else:
        #Error 001
        print("Already exists!")

def data_entry_appliances(owner,appliancename):
    c.execute("INSERT INTO appliances (user,appliance) VALUES(?,?)",(owner,appliancename))
    conn.commit()
def login_password(username):
    c.execute("SELECT password FROM login WHERE user='"+username+"'")
    for row in c.fetchall():
        return row[0]

def appliance_appliances(username):
    c.execute("SELECT appliance from appliances WHERE user='"+username+"'")
    for row in c.fetchall():
        return row[0]

def encrypt(password):
    m = sha512()
    m.update(bytes(password,'utf-8'))
    return m.digest()
def clear_empty_row_login():
    c.execute("SELECT user FROM login")
    c.execute("DELETE FROM login WHERE user IS NULL OR trim(user) = ''")
    conn.commit()
def clear_empty_row_appliances():
    c.execute("SELECT user FROM appliances")
    c.execute("DELETE FROM appliances WHERE user IS NULL OR trim(user) = ''")
    conn.commit()
def verify_login(username, thepassword):
    c.execute("SELECT password FROM login WHERE user = '"+username+"'")
    for row in c.fetchall():
        if row[0]==encrypt(thepassword):
            return 0
        else:
            return -1

#setup_stuff()
#program
#create_table("login")
#create_table2("appliances")
create_table3("reviews")
#data_entry_appliances("Edwin0101","Coffee Machine")
#clear_empty_row_login()
data_entry_login("Edwin","Pawn1234")
#print(appliance_appliances("Edwin0101"))
#print(verify_login("Edwin0101","Pawn1234"))
