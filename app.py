from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return 'hello'

@app.route('/post/<post_id>', methods=['GET', 'POST'])
def post (post_id):
    if request.method == 'GET':
        return 'post: ' + post_id
    elif request.method == 'POST':
        return 'your post is saved'

    