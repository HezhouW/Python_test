from flask import Flask,render_template,request
app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
@app.route('/index',methods = {'GET'})
def index():
	# if request.method != "POST":
	# 	return 'fuck'
	# request.
	user = 'aaha'
	posts = [
	{
	'author': { 'nickname': 'John' },
	'body': 'Beautiful day in Portland!'
	},
	{
	'author': { 'nickname': 'Susan' },
	'body': 'The Avengers movie was so cool!'
	}
		]
	return render_template(
	"index.html",
	title = 'whz',
	USER = user,
	posts = posts
	)
