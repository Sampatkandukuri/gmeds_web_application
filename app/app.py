
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'netmeds'

mysql = MySQL(app)



@app.route('/login',methods=['GET','POST'])
def login():
    #c_id = 1
    if request.method == 'POST':
        #c_id = c_id +1
        userDetails = request.form
        username = userDetails['username']
        password = userDetails['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO log_in(username,password) VALUES(%s,%s)",(username,password))
        mysql.connection.commit()
        cur.close()
        #return 'Success'
        return render_template('homepage.html')

    return render_template('netmeds_login.html')



if __name__ == '__main__':
    app.run(debug=True)