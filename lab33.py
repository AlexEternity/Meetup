from datetime import datetime, date, time
import requests
r = requests.get('https://api.meetup.com/2/open_events?&sign=true&photo-host=public&lat=51.513191&topic=Android&lon=-0.133495&radius=10&page=20&key=2a1476266b7f482b214020761b3159')
res = r.json()
file = open("lab33.html", "w+", encoding='utf-8')
j=0
file.write("<!DOCTYPE HTML><html><head><style>body{background:yellow;}div{font-family:Arial;border:solid;border-radius:20px;background:aquamarine;margin-bottom:10px;box-shadow: 0 0 20px rgba(0,0,0,0.5);}header{margin:-20px;vertical-align:middle;text-align:center;font-size:150%;color:red;}</style></head><body><header><h1>There is a list of occasions for a week</h1></header>")
while j<7:
	if 	j==0:
		file.write("<h1 align='center'>Monday</h1>")
	elif j==1:
		file.write("<h1 align='center'>Tuesday</h1>")
	elif j==2:
		file.write("<h1 align='center'>Wednsday</h1>")
	elif j==3:
		file.write("<h1 align='center'>Thursday</h1>")
	elif j==4:
		file.write("<h1 align='center'>Friday</h1>")
	elif j==5:
		file.write("<h1 align='center'>Saturday</h1>")
	elif j==6:
		file.write("<h1 align='center'>Sunday</h1>")
	for item in res['results']:
		dt=datetime.fromtimestamp(int(item['time'])/1000).weekday()
		if dt == j:
			file.write("<div><p><b>Time: </b>" + str(datetime.fromtimestamp(int(item['time'])/1000))+"</p>\n")
			file.write("<p><b>Name of Occasion: </b>" + str(item['name']+"</p>\n"))
			file.write("<p><b>Organizator: </b>" + str((item['group'])['name'])+"</p>\n")
			file.write("<p><b>Description: </b></p>")
			file.write("<p>"+str(item['description'])+"</p>")
			try:
				file.write("<p><b>Phone: </b>" + str((item['venue'])['phone'])+"</p>\n")
			except KeyError:pass
			try:
				file.write("<p><b>Country: </b>" + str((item['venue'])['localized_country_name'])+"</p>\n")
			except KeyError:pass
			try:
				file.write("<p><b>City: </b>" + str((item['venue'])['city'])+"</p>\n")
			except KeyError:pass
			try:
				file.write("<p><b>Address: </b>" + str((item['venue'])['address_1'])+"</p>\n")
			except KeyError:pass
			try:
				file.write("<p><b>Address2: </b>" + str((item['venue'])['address_2'])+"</p>\n")
			except KeyError:pass
			file.write("</div>")
	j=j+1
file.write("</body></html>")
file.close()