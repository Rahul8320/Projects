from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)

#code for mysql connection
app.config['MYSQL_HOST'] = 'localhost'  #hostname
app.config['MYSQL_USER'] = 'root'       #username
app.config['MYSQL_PASSWORD'] = 'root@8320'       #password
app.config['MYSQL_DB'] = 'Payment'      #database name

mysql = MySQL(app)
@app.route("/")
def index():
	return render_template("PaymentForm.html")

@app.route("/success",methods=['POST'])
def success():
	if 'name' in request.form and 'gender' in request.form and 'address' in request.form and 'email' in request.form and 'pincode' in request.form and 'card' in request.form and 'cardNumber' in request.form and 'expiryDate' in request.form and 'cvv' in request.form:
		name = request.form['name']
		gender = request.form['gender']
		address = request.form['address']
		email = request.form['email']
		pincode = request.form['pincode']
		cardType = request.form['card']
		cardNumber = request.form['cardNumber']
		expiryDate = request.form['expiryDate']
		cvv = request.form['cvv']

		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('INSERT INTO details VALUES (NULL,%s,%s,%s,%s,%s,%s,SHA1(%s),%s,SHA1(%s))',(name,gender,address,email,pincode,cardType,cardNumber,expiryDate,cvv))
		mysql.connection.commit()
		return render_template("complete.html")

	else:
		return ('Error! Payment Not completed!')
