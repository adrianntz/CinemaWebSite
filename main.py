# Store this code in 'app.py' file
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'asdqweas'
app.config['MYSQL_DB'] = 'categories_movies'


mysql = MySQL(app)


@app.route('/')

@app.route("/index")
def index():
   return render_template("index.html")


@app.route('/movieintroduce', methods =['GET', 'POST'])
def movieintroduce():
   msg = ''
   if request.method == 'POST' and 'title' in request.form and 'pg_rating' in request.form and 'budget' in request.form and 'director' in request.form and 'language' in request.form and 'release_date' in request.form and 'avg_reviews' in request.form and 'length' in request.form:
      title = request.form['title']
      pg_rating = request.form['pg_rating']
      budget = request.form['budget']
      director = request.form['director']
      language = request.form['language']
      release_date = request.form['release_date']
      avg_reviews = request.form['avg_reviews']
      length = request.form['length']
      cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
      cursor.execute("INSERT INTO `categories_movies`.`movie` (`Title`, `pg_rating`, `budget`, `Director`, `Language`, `release_date`, `average_reviews`, `length`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(title, pg_rating, budget, director, language, release_date, avg_reviews, length))
      mysql.connection.commit()
      msg = 'You have successfully registered !'
   elif request.method == 'POST':
      msg = 'Please fill out the form !'
   return render_template('movieintroduce.html', msg = msg)

@app.route('/categoryintroduce', methods =['GET', 'POST'])
def categoryintroduce():
   msg = ''
   if request.method == 'POST' and 'name' in request.form and 'target_audience' in request.form and 'setting' in request.form and 'theme' in request.form and 'production' in request.form:
      name = request.form['name']
      target_audience = request.form['target_audience']
      setting = request.form['setting']
      theme = request.form['theme']
      production = request.form['production']
      cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
      cursor.execute("INSERT INTO `categories_movies`.`category` (`name`, `target_audience`, `setting`, `theme`, `production`) VALUES (%s,%s,%s,%s,%s)",(name, target_audience, setting, theme, production))
      mysql.connection.commit()
      msg = 'You have successfully registered !'
   elif request.method == 'POST':
      msg = 'Please fill out the form !'
   return render_template('categoryintroduce.html', msg = msg)

@app.route('/screeningintroduce', methods =['GET', 'POST'])
def screeningintroduce():
   msg = ''
   if request.method == 'POST' and 'idmovie' in request.form and 'idcat' in request.form and 'cinema' in request.form and 'ticket_price' in request.form and 'date' in request.form and 'time' in request.form and 'location' in request.form and 'seats_left' in request.form:
      idmovie = request.form['idmovie']
      idcat = request.form['idcat']
      cinema = request.form['cinema']
      ticket_price = request.form['ticket_price']
      date = request.form['date']
      time=request.form['time']
      location=request.form['location']
      seats_left=request.form['seats_left']
      cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
      cursor.execute("INSERT INTO `categories_movies`.`screening` (`idMovie`, `idCategory`, `cinema`, `ticket_price`, `date`, `time`, `location`, `seats_left`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(idmovie, idcat, cinema, ticket_price, date,time,location,seats_left))
      mysql.connection.commit()
      msg = 'You have successfully registered !'
   elif request.method == 'POST':
      msg = 'Please fill out the form !'
   return render_template('screeningintroduce.html', msg = msg)

@app.route('/categoriesdisplay')
def categoriesdisplay():
    cursor = mysql.connection.cursor()
    users=cursor.execute("SELECT * FROM categories_movies.category")
    if users>0:
        displayVector=cursor.fetchall()
        return render_template('categoriesdisplay.html',displayVector=displayVector)

@app.route('/moviesdisplay')
def moviesdisplay():
    cursor = mysql.connection.cursor()
    users=cursor.execute("SELECT * FROM categories_movies.movie")
    if users>0:
        displayVector=cursor.fetchall()
        return render_template('moviesdisplay.html',displayVector=displayVector)

@app.route('/screeningdisplay')
def screeningdisplay():
    cursor = mysql.connection.cursor()
    users=cursor.execute("SELECT * FROM categories_movies.screening")
    if users>0:
        displayVector=cursor.fetchall()
        return render_template('screeningdisplay.html',displayVector=displayVector)

@app.route('/categorydelete', methods =['GET', 'POST'])
def categorydelete():
   msg = ''
   if request.method == 'POST' and 'idcat' in request.form:
      idcat=request.form['idcat']
      cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
      cursor.execute("delete from categories_movies.category where idCategory=%s;", (idcat,))
      mysql.connection.commit()
      msg = 'You have successfully deleted'
   elif request.method == 'POST':
      msg = 'Please fill out the form !'
   return render_template("categorydelete.html",msg=msg)

@app.route('/moviedelete', methods =['GET', 'POST'])
def moviedelete():
   msg = ''
   if request.method == 'POST' and 'idmovie' in request.form:
      idmovie=request.form['idmovie']
      cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
      cursor.execute("delete from categories_movies.movie where idMovie=%s;", (idmovie,))
      mysql.connection.commit()
      msg = 'You have successfully deleted'
   elif request.method == 'POST':
      msg = 'Please fill out the form !'
   return render_template("moviedelete.html",msg=msg)

@app.route('/screeningdelete', methods =['GET', 'POST'])
def screeningdelete():
   msg = ''
   if request.method == 'POST' and 'idscreening' in request.form:
      idscreening=request.form['idscreening']
      cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
      cursor.execute("delete from categories_movies.screening where idScreening=%s;", (idscreening,))
      mysql.connection.commit()
      msg = 'You have successfully deleted'
   elif request.method == 'POST':
      msg = 'Please fill out the form !'
   return render_template("screeningdelete.html",msg=msg)

@app.route('/categoryupdate', methods=['GET','POST'])
def categoryupdate():
   msg=''
   if request.method == 'POST' and 'idcat' in request.form and 'name' in request.form and 'target_audience' in request.form and 'setting' in request.form and 'theme' in request.form and 'production' in request.form:
      idcat=request.form['idcat']
      name = request.form['name']
      target_audience = request.form['target_audience']
      setting = request.form['setting']
      theme = request.form['theme']
      production = request.form['production']
      cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
      cursor.execute("UPDATE categories_movies.category SET name=%s,target_audience=%s,setting=%s,theme=%s,production=%s WHERE idCategory=%s;",(name, target_audience, setting, theme, production,idcat))
      mysql.connection.commit()
      msg = 'You have successfully updated !'
   elif request.method == 'POST':
      msg = 'Please fill out the form !'
   return render_template('categoryupdate.html', msg = msg)


@app.route('/movieupdate', methods =['GET', 'POST'])
def movieupdate():
   msg = ''
   if request.method == 'POST' and 'idmovie' in request.form and 'title' in request.form and 'pg_rating' in request.form and 'budget' in request.form and 'director' in request.form and 'language' in request.form and 'release_date' in request.form and 'avg_reviews' in request.form and 'length' in request.form:
      idmovie=request.form['idmovie']
      title = request.form['title']
      pg_rating = request.form['pg_rating']
      budget = request.form['budget']
      director = request.form['director']
      language = request.form['language']
      release_date = request.form['release_date']
      avg_reviews = request.form['avg_reviews']
      length = request.form['length']
      cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
      cursor.execute("UPDATE `categories_movies`.`movie` SET `Title` = %s, `pg_rating` = %s, `budget` = %s, `Director` = %s, `Language` = %s, `release_date` = %s, `average_reviews` = %s, `length` = %s WHERE (`idMovie` = %s);",(title, pg_rating, budget, director, language, release_date, avg_reviews, length,idmovie))
      mysql.connection.commit()
      msg = 'You have successfully updated !'
   elif request.method == 'POST':
      msg = 'Please fill out the form !'
   return render_template('movieupdate.html', msg = msg)


@app.route('/moviesANDscreeningdisplay')
def moviesANDscreeningdisplay():
    cursor = mysql.connection.cursor()
    users=cursor.execute("SELECT m.Title, m.pg_rating, m.Language,m.length,s.cinema,s.location,s.date,s.time,s.ticket_price, s.seats_left FROM categories_movies.movie m inner join categories_movies.screening s using (idMovie);")
    if users>0:
        displayVector=cursor.fetchall()
        return render_template('moviesANDscreeningdisplay.html',displayVector=displayVector)


@app.route("/display")
def display():
   if 'loggedin' in session:
      cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
      cursor.execute('SELECT * FROM accounts WHERE id = % s', (session['id'], ))
      account = cursor.fetchone()
      return render_template("display.html", account = account)
   return redirect(url_for('login'))


if __name__ == "__main__":
   app.run(host ="localhost", port = int("5000"))

