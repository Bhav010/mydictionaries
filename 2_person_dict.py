person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)
print()
x = person["pets"].keys()
print(x)

"""
# 1. print name of second child

print(person["children"])
print()
mylist = person["children"]
print(mylist[1])


# 2. print name of the cat

print(person["pets"]["cat"])
# OR
#mylist2 = person["pets"]
#print(mylist2["cat"])

# 3. use loop to print the names of each child
for x in person["children"]:
    print(x)


# 4. use loop to print the pets in following format:
# The type of pet is: dog and the name of pet is: Fido
mylist = person["pets"]
for key, value in mylist.items():
    print(f"The type of pet is: {key} and the name of pet is: {value}")


# print(person["pets"])
dict = person["pets"]
for key, value in dict.items():
    print(f"The type of pet is: {key} and the name of pet is: {value}")
"""
