from flask import Flask, request, url_for, redirect, abort, render_template
import mysql.connector

app = Flask(__name__)
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password12345678_PSW',
    database='prueba'
)

cursor = mydb.cursor(dictionary=True)



@app.route('/hello')
def hello():
    return 'hello'

@app.route('/post/<post_id>', methods=['GET', 'POST'])
def post (post_id):
    if request.method == 'GET':
        return 'post: ' + post_id
    elif request.method == 'POST':
        return 'your post is saved'

@app.route('/', methods=['POST', 'GET'])
def index():
    cursor.execute('select * from Usuario')
    users = cursor.fetchall()
    # abort(403)
    # return redirect(url_for('post', post_id = 33))
    # print(url_for('post', post_id=1))
    # print(request.form)'
    # return render_template('lele.html')
    return render_template("users.html", users = users)

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', msg = 'This is my msg.')


@app.route('/create',  methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        age = request.form['edad']

        query = 'INSERT INTO Usuario (username, email, edad) values (%s, %s, %s)'
        values = (username, email, age)

        cursor.execute(query, values)
        mydb.commit()

        return redirect(url_for('index'))
    return render_template('create.html')