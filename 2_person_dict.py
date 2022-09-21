person = {} #creates an empty dictionary
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

#print(person)

print(person['children'][1]) #prints record[1] from the list of children in the person's dictionary 

print(person['pets']['cat']) #prints the cat's name in the pets dictionary which is in the person's dictionary 

for child in person['children']:
    print(child)

for p in person['pets']:
    print(person['pets'][p])