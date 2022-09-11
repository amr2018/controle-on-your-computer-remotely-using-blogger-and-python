
import requests
from os import system
from bs4 import BeautifulSoup
from time import sleep

def update():
	res = requests.get('your blogger url')
	html = res.content
	soup = BeautifulSoup(html, 'html.parser')
	for div in soup.find_all('div'):
		_class = div.get('class')
		if _class != None:
			if _class[0] == 'c':
				sleep(5)
				system(div.text)

	sleep(5)
	update()

sleep(5)
update()
