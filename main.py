from flask import Flask,render_template,request
import requests
import smtplib

OWN_EMAIL = 'email@mail.com'
OWN_PASSWORD = 'password'

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

@app.route('/contact',methods=['POST','GET'])
def get_contact():
	if request.method == 'POST':
		data = request.form
		send_email(data["name"], data["email"], data["phone"], data["message"])
		return render_template('contact.html')
	return render_template('contact.html')

@app.route('/about')
def get_about():
	return render_template('about.html')

def send_email(name,email,phone,message):
	email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
	with smtplib.SMTP("smtp.gmail.com") as connection:
		connection.starttls()
		connection.login(OWN_EMAIL,OWN_PASSWORD)
		connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)

if __name__ == "__main__":
	app.run(debug=True)


