import sqlite3
from hashlib import *
from flask import *
from flask_cors import CORS, cross_origin

conn = sqlite3.connect('login.db', check_same_thread=False)
c = conn.cursor()
#data=request.get_json()
#data.get(name)
def setup_stuff():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret!'

    # Enable cors (so the development server can access Python back-end (since it has different port number)
    # cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    cors = CORS(app, resources={r"/*": {"origins": "*"}})

    @app.route("/register",methods=['POST'])
    def register_user():
        try:
            data=request.get_json()
            user = data.get("username")
            password = data.get("password")
            data_entry(user,password)
            return "Success"
        except:
            return "Failure"
    @app.route("/login",methods=['GET','POST'])
    def login_user():
        data=request.get_json()
        user=data.get("username")
        passwordtocheck=encrypt(data.get("password"))
        actual = get_password(user)
        if actual==passwordtocheck:
            return "Success"
        else:
            return "Failure"
                
    @app.route('/getappliances', methods=['GET','POST'])
    def woosh():
        data=request.get_json()
        user=data.get("username")
        appliances = get_appliance(user)
        print(jsonify(appliances))
        return appliances

    @app.route('/getreviews', methods=['GET','POST'])
    def reddit():
        data=request.get_json()
        product=data.get("productID")
        reviews=get_review(product)
        print(jsonify(reviews))
        return reviews

    @app.route('/newappliance', methods=['GET','POST'])
    def woooooosh():
        data=request.get_json()
        user=data.get("username")
        appliance=data.get("appliancename")
        data_entry_appliances(user,appliance)
        return "Success"
#user,product,reviews,stars,upvotes
    @app.route('/newreview',methods=['GET','POST'])
    def flexy():
        data=request.get_json()
        user=data.get('username')
        product=data.get('product')
        reviews=data.get('reviews')
        stars=data.get('stars')
        upvotes=data.get('upvotes')
        data_entry_reviews(user,product,reviews,stars,upvotes)
        return "Success"

    @app.route('/pinger', methods=['POST'])
    def ping_ponger():
        data=request.get_json()
        return jsonify(data)

    if __name__ == '__main__':
        #socketio.run(app)
        # app.run(host='0.0.0.0', port=5000)
        app.run()
#setup_stuff()

def nth_repl(s, sub, repl, nth):
    find = s.find(sub)
    # if find is not p1 we have found at least one match for the substring
    i = find != -1
    # loop util we find the nth or we find no match
    while find != -1 and i != nth:
        # find + 1 means we start at the last match start index + 1
        find = s.find(sub, find + 1)
        i += 1
    # if i  is equal to nth we found nth matches so replace
    if i == nth:
        return s[:find]+repl+s[find + len(sub):]
    return s

#####Create Tables#####

def create_table(tablename):
    c.execute("CREATE TABLE IF NOT EXISTS "+tablename+"(user TEXT,password TEXT)")

def create_table2(tablename):
    c.execute("CREATE TABLE IF NOT EXISTS "+tablename+" (user TEXT, appliance TEXT, category TEXT)")         #search by appliance name or category.
    
def create_table3(tablename):
    c.execute("CREATE TABLE IF NOT EXISTS "+tablename+" (user TEXT, productID INT, review TEXT, stars INT,upvotes INT)")
#####Data Entry#####

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
    isInAppliances=False
    c.execute("SELECT appliance FROM appliances")
    for row in c.fetchall():
        if row[0]==appliancename:
            isInAppliances=True
            break
    if isInAppliances==False:
        c.execute("INSERT INTO appliances (user,appliance) VALUES(?,?)",(owner,appliancename))
    conn.commit()

def data_entry_reviews(user,product,reviews,stars,upvotes):
    hasReviewed=False
    c.execute("SELECT productID, review, stars, upvotes FROM reviews")
    for row in c.fetchall():
        if row[0]==get_review(user)[1] and user==get_review(user)[0]:
            hasReviewed=True
    if hasReviewed==False:
        c.execute("INSERT INTO reviews (user,productID,review,stars,upvotes) VALUES(?,?,?,?,?)",(user,product,reviews,stars,upvotes))
    conn.commit()

#####Get information#####    
def get_password(username):
        c.execute("SELECT user,password from login WHERE user='"+username+"'")
        for row in c.fetchall():
            return row[1]
def get_appliance(username):
    rows=[]
    returner='[ ["'+username+'"],'
    for i in range(1,2):
        c.execute("SELECT user,appliance from appliances WHERE user='"+username+"'")
        for row in c.fetchall():
            returner+=',"'+row[i]+'"'.replace(",","",1)
    returner+="]]"
    returner=nth_repl(returner,",","",2)
    return returner
def get_review(productID):
    returner='[ ["'+str(productID)+'"]'
    for i in range(2,5):
        returner+="["
        c.execute("SELECT user,productID,review,stars,upvotes from reviews WHERE productID="+str(productID))
        for row in c.fetchall():
            returner+=',"'+str(row[i])+'"'.replace(",","",1)
            returner+="],"
        returner=nth_repl(returner,",","",returner.count(",")).replace("[,",",[")
        returner+="]"
    return returner
        

#####Clear Empty Rows#####

def clear_empty_row_login():
    c.execute("SELECT user FROM login")
    c.execute("DELETE FROM login WHERE user IS NULL OR trim(user) = ''")
    conn.commit()
    
def clear_empty_row_appliances():
    c.execute("SELECT user FROM appliances")
    c.execute("DELETE FROM appliances WHERE user IS NULL OR trim(user) = ''")
    conn.commit()
    
def clear_empty_row_reviews():
    c.execute("SELECT user FROM reviews")
    c.execute("DELETE FROM reviews WHERE user IS NULL OR trim(user) = ''")
    conn.commit()

#####Login#####    

def verify_login(username, thepassword):
    c.execute("SELECT password FROM login WHERE user = '"+username+"'")
    for row in c.fetchall():
        if row[0]==encrypt(thepassword):
            return 0
        else:
            return -1
    
def encrypt(password):
    m = sha512()
    m.update(bytes(password,'utf-8'))
    return m.digest()



#setup_stuff()
def setup_tables():
    create_table("login")
    create_table2("appliances")
    create_table3("reviews")
def insertData():
    data_entry_appliances("Edwin0101","Coffee Machine")
    data_entry_login("orangeyf","pawn")
    data_entry_reviews("Edwin0101",34562,"Not good. 1 star.",5,23)

#program
#setup_stuff()
setup_tables()
#insertData()
#print(get_appliance("Edwin0101")[1])
#print(verify_login("Edwin0101","Pawn1234"))

'''
[
    [
        "Edwin0101",
        "Coffee Machine"
    ],
    [
        "Edwin0101",
        "Coffee Machine"
    ],
    [
        "Edwin0101",
        "Coffee Machine"
    ],
    [
        "Edwin0101",
        "Coffee Machine"
    ]
]
'''
