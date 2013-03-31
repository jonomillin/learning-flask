from flask import Flask, url_for, request
app = Flask(__name__)

@app.route('/')
def index():
	br = '</br>'
	str = "List: " + br
	str += url_for('login') + br
	str +=  url_for('login', next ='/') + br
	str +=  url_for('profile', username='John Doe')
	return 'Index Page...' + str

@app.route('/hello/')
def hello():
	return 'Hello World! Whoop!!'

@app.route('/login/', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		return 'You just posted something!'
	else:
		return 'Time to see the Login form.'

@app.route('/user/<username>/')
def profile(username):
	return 'Hello %s!!' %username

if __name__ == '__main__':
	app.debug = True
	app.run()
	# app.run(host='0.0.0.0') # Run publicly...
