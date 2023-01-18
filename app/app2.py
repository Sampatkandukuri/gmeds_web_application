
from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import random

app = Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'netmeds'

mysql = MySQL(app)

@app.route('/',methods=['GET','POST'])
def index():
    
    if request.method == 'POST':
        global c_id
        c_id = random.randint(10000,99999)
        userDetails = request.form
        name = userDetails['name']
        gender = userDetails['gender']
        age = userDetails['age']
        address = userDetails['address']
        mobile = userDetails['mobile']
        email = userDetails['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO customers(c_id,c_name,gender,age,address,contact,email) VALUES(%s,%s,%s,%s,%s,%s,%s)",(c_id,name,gender,age,address,mobile,email))
        mysql.connection.commit()
        cur.close()
        return render_template("netmeds_login.html")

    return render_template('registration.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        
        global c_id
        
        userDetails = request.form
        username = userDetails['username']
        password = userDetails['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO log_in(c_id,username,password) VALUES(%s,%s,%s)",(c_id,username,password))
        mysql.connection.commit()
        cur.close()
        #return 'Success'
        return render_template('homepage.html')

    return render_template('netmeds_login.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template("homepage.html")



@app.route('/cart.html', methods=['GET', 'POST'])
def cart():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM cart")
    data = cur.fetchall()
    return render_template('netmeds_cart.html', data=data)
    #return render_template('netmeds_cart.html')
'''
@app.route('/order.html', methods=['GET', 'POST'])
def order():
    cur = mysql.connection.cursor()
    
    return render_template('order.html')
'''

@app.route('/clear', methods=['GET', 'POST'])
def clear():
    cur = mysql.connection.cursor()
    cur.execute("TRUNCATE TABLE cart")
    data = cur.fetchall()
    return render_template('netmeds_cart.html', data=data)


@app.route('/add1',methods=['GET','POST'])
def add1():
    if request.method == 'POST':
        userDetails = request.form
        
        #pr1 = userDetails['pr1']
        #co1 = userDetails['co1']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO cart(product,cost) VALUES('Thermometer','Rs:200')")
        mysql.connection.commit()
        cur.close()
        return render_template('homepage.html')
    return render_template('homepage.html')


@app.route('/add2',methods=['GET','POST'])
def add2():
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO cart(product,cost) VALUES('Dolo-650mg','Rs:75')")
        mysql.connection.commit()
        cur.close()
        return render_template('homepage.html')
    return render_template('homepage.html')

@app.route('/add3',methods=['GET','POST'])
def add3():
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO cart(product,cost) VALUES('Benadryl Cough Syrup(50ml)','Rs:250')")
        mysql.connection.commit()
        cur.close()
        return render_template('homepage.html')
    return render_template('homepage.html')

@app.route('/add4',methods=['GET','POST'])
def add4():
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO cart(product,cost) VALUES('Band-aid(Assorted 100)','Rs:100')")
        mysql.connection.commit()
        cur.close()
        return render_template('homepage.html')
    return render_template('homepage.html')

@app.route('/add5',methods=['GET','POST'])
def add5():
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO cart(product,cost) VALUES('Amoxicillin Capsules IP,500mg','Rs:200')")
        mysql.connection.commit()
        cur.close()
        return render_template('homepage.html')
    return render_template('homepage.html')

@app.route('/add6',methods=['GET','POST'])
def add6():
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO cart(product,cost) VALUES('Azithromycin Tablet IP, 20 X 3 Tablets','Rs:70')")
        mysql.connection.commit()
        cur.close()
        return render_template('homepage.html')
    return render_template('homepage.html')

@app.route('/add7',methods=['GET','POST'])
def add7():
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO cart(product,cost) VALUES('Reusable Asiapacific N95 Mask','Rs:20')")
        mysql.connection.commit()
        cur.close()
        return render_template('homepage.html')
    return render_template('homepage.html')


@app.route('/add8',methods=['GET','POST'])
def add8():
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO cart(product,cost) VALUES('Cetirizine Tablet 10mg','Rs:349')")
        mysql.connection.commit()
        cur.close()
        return render_template('homepage.html')
    return render_template('homepage.html')


@app.route('/payment',methods=['GET','POST'])
def pay():
    if request.method == 'POST':

        return render_template('payments.html')
    return render_template('netmeds_cart.html')



@app.route('/orders',methods=['GET','POST'])
def orders():
    if request.method == 'POST':
        global c_id,order_id
        userDetails = request.form
        #print(userDetails)[0][0]
        firstname = userDetails['firstname']
        email = userDetails['email']
        address = userDetails['address']
        city = userDetails['city']
        
        cardname = userDetails['cardname']
        cardnumber = userDetails['cardnumber']
        expmonth = userDetails['expmonth']
        expyear = userDetails['expyear']
        cvv = userDetails['cvv']



        order_id = random.randint(100000,999999)
        #t= (firstname,email, address, city)
        #t= (firstname,email, address, city, state, state, zip,  cardname, cardnumber, expmonth,expyear,cvv)
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO payments(c_id,order_id,firstname,email, address, city,cardname, cardnumber, expmonth,expyear,cvv) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(c_id,order_id,firstname,email, address, city,cardname, cardnumber, expmonth,expyear,cvv))
        cur.execute("INSERT INTO orders(c_id,order_id,name,email, address,status ) VALUES(%s,%s,%s,%s,%s,'Order placed successfully')",(c_id,order_id,firstname,email,address))
        cur.execute("TRUNCATE TABLE cart")
        mysql.connection.commit()
        cur.close()
        return render_template('homepage.html')
    return render_template('payments.html')

@app.route('/order.html', methods=['GET', 'POST'])
def order2():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM orders")
    data = cur.fetchall()
    return render_template('order.html', data=data)


if __name__ == '__main__':
    c_id = random.randint(10000,99999)
     
    app.run(debug=True)