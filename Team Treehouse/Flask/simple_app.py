from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name='Treehouse'):
	return "Hello from {}".format(name)

@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
def add(num1, num2):
	return '{} + {} = {}'.format(num1, num2, num1+num2)

#This port and host are specific to treehouse.
app.run(debug=true, port = 8000, host='0.0.0.0')