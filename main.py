from os import abort
from flask import Flask, jsonify, render_template, request
# from requests import request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
    # return 'Hello, world'

# create api for add function

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return jsonify({'result': num1 + num2})

# create api for subtract function


@app.route('/subtract/<int:num1>/<int:num2>')
def subtract(num1, num2):
    return jsonify({'result': num1 - num2})

# create a post method to return something in json format


@app.route('/post/<string:name>/<int:age>', methods=['GET', 'Post'])
def post(name, age):
    data = {
        'name': name,
        'age': age,
    }
    return jsonify({'result': data})

# define a function which takes both get and post method


@app.route('/get_post/<string:name>/<int:age>', methods=['GET', 'POST'])
def get_post(name, age):
    data = {
        'name': name,
        'age': age,
    }
    if request.method == 'POST':

        return jsonify({'result': data})
    else:
        return jsonify({'result': 'GET method'})


@app.route('/get_post2', methods=['GET', 'POST'])
def get_post2():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        data = {
            'name': name,
            'age': age,
        }
        return jsonify({'result': data})
    else:
        return jsonify({'result': 'GET method'})

# create a function to abort the request


@app.route('/abort/<int:num>')
def abort(num):
    if num == 1:
        return 'Hello, world'
    else:
        abort(404)

# create a function to return a template


@app.route('/template')
def template():
    return render_template('index.html')

# create a end of api which will display the details of person when eneterd id


@app.route('/person/<int:id>')
def person(id):
    person = {
        1: {'name': 'John', 'age': 25},
        2: {'name': 'Jane', 'age': 30},
        3: {'name': 'Jack', 'age': 35},
    }
    return jsonify({'result': person[id]})

# create end so that all the persons in list will display


@app.route('/persons')
def persons():
    persons = [
        {'name': 'John', 'age': 25},
        {'name': 'Jane', 'age': 30},
        {'name': 'Jack', 'age': 35},
    ]
    return jsonify({'result': persons})


if __name__ == '__main__':
    app.run(debug=True)
    app.run(port=8000)
