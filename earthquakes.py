"""the eq_data file is a json file that contains detailed information about
earthquakes around the world for a period of a month.

NOTE: No hard-coding allowed except for keys for the dictionaries

1) print out the number of earthquakes

2) iterate through the dictionary and extract the location, magnitude, 
   longitude and latitude of the location and put it in a new
   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a 
   magnitude > 6. Print out the new dictionary.

3) using the eq_dict dictionary, print out the information as shown below (first three shown):

Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364


Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604


Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628

"""

import json

infile = open("eq_data.json", "r")
earthquake1 = json.load(infile)
len1 = len(earthquake1)
print(f"***** #1. The number of earthquakes: {len1} *****")
print()

mylist = earthquake1["features"]
mylist2 = []

for i in mylist:
    eq_dict1 = {}
    if (i["properties"]["mag"]) > 6:
        eq_dict1["Location"] = i["properties"]["place"]
        eq_dict1["Magnitude"] = i["properties"]["mag"]
        eq_dict1["Coordinates"] = i["geometry"]["coordinates"]
        mylist2 += [eq_dict1]

eq_dict = {}
eq_dict["New Dict"] = mylist2
print("***** #2.  New Dictionary   ***** \n")
print(eq_dict)
print()

print("***** #3. Selected output  ***** \n")
for x in mylist2[0:3]:
    print(f"Location: {x['Location']}")
    print(f"Magnitude: {x['Magnitude']}")
    print(f"Longitude: {x['Coordinates'][0]}")
    print(f"Latitude: {x['Coordinates'][1]}")
    print()
