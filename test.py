# import requests
from pprint import pprint 
from bs4 import BeautifulSoup

url = requests.get("https://www.giveindia.org/certified-indian-ngos")
soup = BeautifulSoup(url.text, "html.parser")
dictionary = {}
trs = soup.find("table", class_="table table-bordered")
tr =trs.find("tbody")
tds = tr.find_all("tr")
place = []
work = []
name = []
for i in tds:
	a = i.find_all("td")
	name.append(a[0].getText())
	work.append(a[1].getText())
	place.append(a[2].getText())
dictionary["name"] = name
dictionary["work"] = work
dictionary["place"] = place
pprint (dictionary)
