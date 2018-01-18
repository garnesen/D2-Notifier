import urllib2
from bs4 import BeautifulSoup
from datetime import date
from datetime import timedelta

## The dish to search for
DISH = "Creme Brulee"

# Create the URL
today = date.today()
check_date = today + timedelta(days=2)
url_date = str(check_date.month) + '%2f' + str(check_date.day) + '%2f' + str(check_date.year)
url = 'http://foodpro.dsa.vt.edu/menus/MenuAtLocation.aspx?locationNum=15&naFlag=1&myaction=read&dtdate=' + url_date

# Open the URL
page = urllib2.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

# Check if the item is on the menu
dinner_menu = soup.find('div', attrs={'id': 'meal_3'})
if dinner_menu is not None and DISH in dinner_menu.text:
	print DISH + " on the menu on " + str(check_date) + "!"
else:
	print DISH + " not on the menu on " + str(check_date) + "."
