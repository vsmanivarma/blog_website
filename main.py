from flask import Flask,render_template
import requests
import json
blog_list = requests.get('https://api.npoint.io/12c85ddd76bcc94e3137').json()

app = Flask(__name__)

@app.route('/home')
@app.route('/')
def home():
	return render_template('index.html',blog_list=blog_list)

@app.route('/post/<int:id>')
def get_posts(id):
	requested_post = None
	for blog in blog_list:
		if blog['id'] == id:
			requested_post = blog
	return render_template('post.html', the_blog=requested_post)



@app.route('/contact')
def get_contact():
	return render_template('contact.html')

@app.route('/about')
def get_about():
	return render_template('about.html')

if __name__ == "__main__":
	app.run(debug=True)


