# own definition of all data types as learned in swift as well

# list: list is an ordered collection of multiple data types and it it mutable

# tuple: tuple is an ordered collection of multiple data types and immutable means cannot modify

# dictionary: dictionaries are ordered collection of key-value pairs of multiple data types and mutable

# set: set is an unordered collection of multiple data types and rejects duplicats means only unique values

# data type not goes to variables it always goes to reference value in memory


myList = ["one",["two",3], 4.5] #mutable, it shares the reference if new same datatype is copied this

print("mylist 0 index: ",myList[0])
myList[0] = "ONE"

print("modified list 0 index: ",myList[0])

myTuple = ("Rohit","Alex","sam",9999) #immutable
print("myTuple 0 index: ",myTuple[0])
myList[0] = "jon"

print("modified tuple 0 index: ",myTuple[0])

print("nice practice.")