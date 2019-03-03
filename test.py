# import requests
# from pprint import pprint 
# from bs4 import BeautifulSoup

# url = requests.get("https://www.giveindia.org/certified-indian-ngos")
# soup = BeautifulSoup(url.text, "html.parser")
# dictionary = {}
# trs = soup.find("table", class_="table table-bordered")
# tr =trs.find("tbody")
# tds = tr.find_all("tr")
# place = []
# work = []
# name = []
# for i in tds:
# 	a = i.find_all("td")
# 	name.append(a[0].getText())
# 	work.append(a[1].getText())
# 	place.append(a[2].getText())
# dictionary["name"] = name
# dictionary["work"] = work
# dictionary["place"] = place
# pprint (dictionary)


# names = [{'name': 'Pralhad', 'age': 17},
#  {'name': 'Bhavnesh', 'age': 25},
#  {'name': 'Bhavnesh', 'age': 20},
#  {'name': 'Anoop', 'age': 19},
#  {'name': 'Rishabh', 'age': 24},
#  {'name': 'Rishabh', 'age': 24},
#  {'name': 'Bhavnesh', 'age': 18},
#  {'name': 'Pralhad', 'age': 25},
#  {'name': 'Anoop', 'age': 16},
#  {'name': 'Bhavnesh', 'age': 21},
#  {'name': 'Bhavnesh', 'age': 21},
#  {'name': 'Anoop', 'age': 19},
#  {'name': 'Anoop', 'age': 23},
#  {'name': 'Anoop', 'age': 16},
#  {'name': 'Rishabh', 'age': 17},
#  {'name': 'Bhavnesh', 'age': 17},
#  {'name': 'Rishabh', 'age': 15},
#  {'name': 'Anurag', 'age': 19},
#  {'name': 'Bhavnesh', 'age': 20},
#  {'name': 'Rishabh', 'age': 24},
#  {'name': 'Anoop', 'age': 23},
#  {'name': 'Anurag', 'age': 25},
#  {'name': 'Bhavnesh', 'age': 19},
#  {'name': 'Pralhad', 'age': 18},
#  {'name': 'Anoop', 'age': 16},
#  {'name': 'Anoop', 'age': 25},
#  {'name': 'Rishabh', 'age': 23},
#  {'name': 'Anoop', 'age': 23},
#  {'name': 'Anurag', 'age': 23},
#  {'name': 'Bhavnesh', 'age': 22},
#  {'name': 'Anurag', 'age': 20},
#  {'name': 'Rishabh', 'age': 20},
#  {'name': 'Pralhad', 'age': 25},
#  {'name': 'Pralhad', 'age': 16},
#  {'name': 'Rishabh', 'age': 23},
#  {'name': 'Anoop', 'age': 16},
#  {'name': 'Rishabh', 'age': 16},
#  {'name': 'Pralhad', 'age': 23},
#  {'name': 'Rishabh', 'age': 19},
#  {'name': 'Pralhad', 'age': 20},
#  {'name': 'Anoop', 'age': 22},
#  {'name': 'Rishabh', 'age': 16},
#  {'name': 'Rishabh', 'age': 15},
#  {'name': 'Pralhad', 'age': 15},
#  {'name': 'Pralhad', 'age': 20},
#  {'name': 'Pralhad', 'age': 18},
#  {'name': 'Rishabh', 'age': 18},
#  {'name': 'Anoop', 'age': 15},
#  {'name': 'Anoop', 'age': 16},
#  {'name': 'Anoop', 'age': 19},
#  {'name': 'Anurag', 'age': 20},
#  {'name': 'Rishabh', 'age': 17},
#  {'name': 'Bhavnesh', 'age': 17},
#  {'name': 'Pralhad', 'age': 25},
#  {'name': 'Pralhad', 'age': 25},
#  {'name': 'Rishabh', 'age': 18},
#  {'name': 'Rishabh', 'age': 20},
#  {'name': 'Bhavnesh', 'age': 18},
#  {'name': 'Anoop', 'age': 22},
#  {'name': 'Anurag', 'age': 15},
#  {'name': 'Rishabh', 'age': 18},
#  {'name': 'Pralhad', 'age': 18},
#  {'name': 'Bhavnesh', 'age': 17},
#  {'name': 'Anurag', 'age': 25},
#  {'name': 'Anoop', 'age': 23},
#  {'name': 'Anoop', 'age': 15},
#  {'name': 'Pralhad', 'age': 19},
#  {'name': 'Rishabh', 'age': 21},
#  {'name': 'Anurag', 'age': 18},
#  {'name': 'Anurag', 'age': 21},
#  {'name': 'Pralhad', 'age': 23},
#  {'name': 'Anurag', 'age': 16},
#  {'name': 'Pralhad', 'age': 21},
#  {'name': 'Pralhad', 'age': 25},
#  {'name': 'Anurag', 'age': 16},
#  {'name': 'Rishabh', 'age': 22},
#  {'name': 'Bhavnesh', 'age': 16},
#  {'name': 'Pralhad', 'age': 20},
#  {'name': 'Bhavnesh', 'age': 17},
#  {'name': 'Pralhad', 'age': 22},
#  {'name': 'Bhavnesh', 'age': 21},
#  {'name': 'Anurag', 'age': 20},
#  {'name': 'Pralhad', 'age': 16},
#  {'name': 'Rishabh', 'age': 24},
#  {'name': 'Pralhad', 'age': 18},
#  {'name': 'Rishabh', 'age': 23},
#  {'name': 'Rishabh', 'age': 19},
#  {'name': 'Rishabh', 'age': 21},
#  {'name': 'Pralhad', 'age': 23},
#  {'name': 'Rishabh', 'age': 15},
#  {'name': 'Bhavnesh', 'age': 17},
#  {'name': 'Anurag', 'age': 17},
#  {'name': 'Pralhad', 'age': 24},
#  {'name': 'Anurag', 'age': 15},
#  {'name': 'Pralhad', 'age': 25},
#  {'name': 'Bhavnesh', 'age': 24},
#  {'name': 'Anoop', 'age': 23},
#  {'name': 'Pralhad', 'age': 25},
#  {'name': 'Bhavnesh', 'age': 22},
#  {'name': 'Anoop', 'age': 25}]

# All_names = {}
# for i in names:
# 	if i["name"] not in All_names:
# 		All_names[i["name"]] = {}
# for j in All_names:
# 	for k in names:
# 		if k["name"] == j:
# 			a = All_names[j]
# 			b = k["age"]
# 			if b not in a:
# 				a[b] = 1
# 			else:
# 				a[b] += 1
# pprint (All_names)


S="hedviuoclateion"
D={"evil","chelation","education","violation","lion"}
names = []
length_of_names = []
for i in D:
	# print (i)
	a = ""
	for j in i:
		# print ("-" + j)
		if j in S:
			a += j
	length = 0	
	if i == a:
		names.append(i)
		length = len(i)
		length_of_names.append(length)
max1 = length_of_names[0]
for j in length_of_names:
	if max1 < j:
		max1 = j
for k in length_of_names:
	if k == max1:
		max_length = length_of_names.index(max1)
		print (names[max_length])
		break

