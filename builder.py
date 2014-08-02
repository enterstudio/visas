import os
import json
import datetime

data = {
	"type" : "FeatureCollection",
	"features": []
}
bfolder = "data"
for file in os.listdir(bfolder):
	if file.endswith(".geo.json"):
		with open(bfolder + "/"+ file) as f:
			data["features"].append(json.loads(f.read())["features"][0])


with open("dist/world.geo.json", "w") as w:
	w.write(json.dumps(data))

with open("world.geo.json", "w") as w:
	w.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))

with open("countries.json") as f:
	with open("dist/countries.json","w") as w:
		w.write(json.dumps(json.loads(f.read())))