import urllib2
from bs4 import BeautifulSoup
from datetime import date
from datetime import timedelta
import os
import requests

DISH = "Creme Brulee"
TILL_URL = os.environ.get("TILL_URL")

# Sends the alert using Till
def sendAlert(text):
	print "Sending alert msg: " + text
	requests.post(TILL_URL, json={
		"phone": ["14439758176"],
		"text": text
	})

# Create the URL
today = date.today()
check_date = today + timedelta(days=1)
url_date = str(check_date.month) + '%2f' + str(check_date.day) + '%2f' + str(check_date.year)
url = 'http://foodpro.dsa.vt.edu/menus/MenuAtLocation.aspx?locationNum=15&naFlag=1&myaction=read&dtdate=' + url_date

# Open the URL
page = urllib2.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

# Check if the item is on the menu
dinner_menu = soup.find('div', attrs={'id': 'meal_3'})
if dinner_menu is not None and DISH in dinner_menu.text:
	sendAlert(DISH + " is on the menu on " + str(check_date) + "!")
else:
	print DISH + " is not on the menu on " + str(check_date) + "."
