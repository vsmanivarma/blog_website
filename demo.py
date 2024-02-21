import requests

blog_list = requests.get('https://api.npoint.io/12c85ddd76bcc94e3137').json()
for item in blog_list:
	index = item.id
	print(index)
