import requests
from threading import Thread

data = {'key': 'value'}

def function(para):
	pass

def get(url, content):
	r = requests.get(url, headers=data)
	if r.status_code == 200:
		content.append(r.text)
		print(r.text)
		return r.text

result = []  # to store the result from a thread
th = []  # control the main thread


for i in range(num)
	url = 'http://www.example.com' + str(i)  # or others
	t = Thread(target=get, args=(url, result)
	t.start()
	th.append(t)


for t in th:
	t.join()

