from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
	return '<h1>Welcome to Employee Manager</h1><p>Click <a href="/registration">here</a> to register a new employee or <a href="/information">here</a> to view employee information.</p>'

@app.route('/registration')
def registration():
	return '<h1>Employee Registration</h1><p>Fill out the form below to resgister a new employee.</p><form><label>First Name:</label><input type="text" name="first_name"><br><label>Last Name:</label><input type="text" name="last_name"><br><label>Email:</label><input type="email" name="email"><br><input type="submit" value="Register"></form>'

@app.route('/information')
def information():
	return '<h1>Employee Information</h1><table><tr><th>First Name</th><th>Last Name</th><th>Email</th></tr><tr><td>John</td><td>Doe</td><td>john.doe@example.com</td></tr><tr><td>Jane</td><td>Smith</td><td>jane.smith@example.com</td></tr></table>'

if __name__ == '__main__':
	app.run()
