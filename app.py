from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_USER'] = 'sql6501874'
app.config['MYSQL_PASSWORD'] = 'HlI4TISMfE'
app.config['MYSQL_HOST'] = 'sql6.freemysqlhosting.net'
app.config['MYSQL_DB'] = 'sql6501874'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['MYSQL_PORT'] = 3306
mysql = MySQL(app)

#@app.route('/')
#def home():
    # return render_template("index.html")

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    # cur.execute(''' CREATE TABLE EXAMPLE (id integer, name varchar(20))''')
    # cur.execute('''CREATE TABLE CONTACTS (name varchar(50),email varchar(100),phone integer, subject varchar(500))''')
    cur.execute(''' Insert into CONTACTS values('Anwesh','anweshshaw1@gmail.com',7559140333,'Hi')''')
    cur.execute(''' Insert into CONTACTS values('Arpit','arpit@gmail.com',8682405569,'Hello')''')
    cur.execute(''' Insert into CONTACTS values('Syed','syed856@gmail.com',8782505569,'I donate 20$')''')
    # mysql.connection.commit()
    cur.execute(''' SELECT * FROM CONTACTS ORDER BY name DESC''')
    results = cur.fetchall()
    print(results)
    return results[2]

if __name__ == "__main__":
    app.run(debug=True)
