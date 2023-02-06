import random


phonebook = {"Chris": "555−1111", "Katie": "555−2222", "Joanne": "555−3333"}

"""
print()
print("*****  start section 1 - print dictionary ********")
print()


print(type(phonebook))
print(len(phonebook))

mydictionary = dict(m=9, n=10)
print(mydictionary)
print(len(mydictionary))

print()
print("*****  end section 1 ********")
print()


print()
print("*****  start section 2 - search dictionary ********")
print()


# print(phonebook["Chris"])
# print(phonebook["chris"])

name = "chris"

if name in phonebook:
    print(phonebook[name])
else:
    print(f"{name} is not in phonebook")

print()
print("*****  end section 2 ********")
print()



print()
print("*****  start section 3 - edit/append dictionary ********")
print()

print(phonebook)

phonebook["Chris"] = "555-0123"
phonebook["Joe"] = "555-4444"

print("Updated Dictionary: ")
print(phonebook)


print()
print("*****  end section 3 ********")
print()



print()
print("*****  start section 4 - delete/remove from dictionary ********")
print()

print(phonebook)

del phonebook["Katie"]

print("Updated Dictionary: ")
print(phonebook)

print()
print("*****  end section 4 ********")
print()



print()
print("*****  start section 5 - iterate through keys, values, items ********")
print()


for key in phonebook:
    print(key)  # by default, iteration happens through key

for v in phonebook.values():  # method to print values
    print(v)

for k, v in phonebook.items():

    print(f"the key:{k} and the value:{v}")


for key in phonebook:
    print(phonebook[key])

print()
print("*****  end section 5 ********")
print()


print()
print("*****  start section 6 - using get and clear ********")
print()

phone = phonebook.get("Chris", "555-6789")              #if key not found, this value will be returned
print(phone)


phonebook.clear() 
print(phonebook)

print()
print("*****  end section 6 ********")
print()


print()
print("*****  start section 7 - using pop method ********")
print()

r = phonebook.pop(    "Chris", "not found")  # assign value of key (Chris) to variable(remove)
print(r)                    # print remove
print(phonebook)

print()
print("*****  end section 7 ********")
print()


print()
print("*****  start section 8 - using popitem ********")
print()

print(phonebook)
a = phonebook.popitem()  # pop's the last item in dictionary
print(f"Pop out {a}")
print(phonebook)

print()
print("*****  end section 8 ********")
print()

"""

print()
print("*****  start section 9 - using random and converting to list ********")
print()

print(phonebook)
list_of_keys = list(phonebook)
print(list_of_keys)

print()
random_key = random.choice(list_of_keys)
print(phonebook[random_key])

#print(phonebook[random.choice(list(phonebook))])  # compress above 4 commands in one

print()
print("*****  end section 9 ********")
print()


