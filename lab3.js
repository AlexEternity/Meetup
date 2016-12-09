var request = require('request');
var fs = require('fs');
var str = "";
request('https://api.meetup.com/2/open_events?&sign=true&photo-host=public&lat=51.513191&topic=Android&lon=-0.133495&radius=10&page=20&key=2a1476266b7f482b214020761b3159', function (err,res,body) {
	if (err) throw err;
	var events = (JSON.parse(body))["results"];
	var DayMs = 86400000;
	var starts = (new Date()).setHours(0, 0, 0, 0) + 43200000;
	str+='<!DOCTYPE HTML><html><head><style>body{background:yellow;}div{font-family:Arial;border:solid;border-radius:10px;background:aquamarine;margin-bottom:10px;box-shadow: 0 0 20px rgba(0,0,0,0.5);}header{margin:-20px;vertical-align:middle;text-align:center;font-size:150%;color:red;}</style></head><body><header><h1>There is a list of occasions for a week</h1></header>';
	for (var j = 0; j < 7; j++) {
		str += "<h2>" + (new Date(starts)).toDateString() + "</h2><br>";
		for (var i in events) {
			var eDate = new Date((events[i])["time"]);
			if (eDate > starts && eDate < starts + DayMs) {
				str+="<div>";
				str += "<b>Name: </b>" + (events[i])["name"] + "<br>";
				if ("venue" in events[i]) {
					str += "<b>Address: </b>" + ((events[i])["venue"])["address_1"] + "<br>";
				}
				str += "<b>Time: </b>" + (eDate.toTimeString()).substring(0,5) + " PM<br>";
				if ("description" in events[i]) {
					str +="<details><summary><b>Description</b></summary><p>" + (events[i])["description"] + "</p></details>";
				}
				str += "<br>";
				str+="</div>";
			}
		}
		starts += DayMs;
	}
	str+="</body></html>";
	fs.writeFile("index.html", str, function(err) {
   		if (err) console.log(err);
	});
});

