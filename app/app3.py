
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'netmeds'

mysql = MySQL(app)



@app.route('/',methods=['GET','POST'])
def index():    

    return render_template('homepage.html')


if __name__ == '__main__':
    app.run(debug=True)