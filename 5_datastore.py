# Below is a dictionary that contains information about real estate space for
# a doctor's office. Using the dictionary, create a csv file that has details
# for each space represented as rows. Name your file 'retail_space.csv.

import csv

"""
Your final output should look like:

room-number,use,sq-ft,price
100,reception,50,75
101,waiting,250,75
102,examination,125,150
103,examination,125,150
104,office,150,100

"""
datastore = {
    "medical": [
        {"room-number": 100, "use": "reception", "sq-ft": 50, "price": 75},
        {"room-number": 101, "use": "waiting", "sq-ft": 250, "price": 75},
        {"room-number": 102, "use": "examination", "sq-ft": 125, "price": 150},
        {"room-number": 103, "use": "examination", "sq-ft": 125, "price": 150},
        {"room-number": 104, "use": "office", "sq-ft": 150, "price": 100},
    ]
}

outfile = open("retail_space.csv", "w")
outfile.write("room-number, use,sq-ft,price \n")

mylist = datastore["medical"]  # list
for y in mylist[0:2]:
    print(y["room-number"])
"""
x = ""
for i in mylist:
    for j in i:
        x += j + ""
    outfile.write(
        str((i["room-number"]))
        + ","
        + (i["use"])
        + ","
        + str(i["sq-ft"])
        + ","
        + str(i["price"])
        + "\n"
    )

outfile.close()
"""

"""

mydict = {}
for i in mylist:
    for k, v in mydict:
        mylist = mydict[k, v]
        print(mydict.values())
        print()
"""

""" Working Code
mylist = datastore["medical"]  # list
key_var = []
val_var = []

for i in mylist:
    val = []
    for k, v in i.items():
        key_var.append(k)
        val.append(v)
    val_var.append(val)

print(list(dict.fromkeys(key_var)))
for v in val_var:
    print(v)
 #Working Code Ends
"""

"""
#Practise
mylist = datastore["medical"]  # list
for dicts in mylist:
    print(mylist.get("room-number")),
    print(mylist.get("use")),
    print(mylist.get("sq-ft")),



for i in mylist:
    print(i.keys())
    print(i.values())
    print()

for i in range(5):
    for j in range(5):
        print(mylist[i], end=" ")
        print()
"""

# x = mydict.keys()
# print(x)

# for key in mydict:
#     print(mydict)
#     print()
