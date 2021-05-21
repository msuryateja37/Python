# Dictionaries are a type of collection in Python.
# A dictionary has keys and values.
# The key is analogous to the index, they are like addresses but they don’t have to be
# integers. They are usually characters; the values are
# similar to the elements in a list and contain information.
myDict = {"surya":5, "teja":4, "python":6}
print(type(myDict))
print(myDict)

print(myDict["surya"]) # keys are used to acesse the data

myDict["rock"] = 4 # Adding new data to dictionary
print(myDict)

del(myDict["teja"]) # Deleting a dictionary Item
print(myDict)

val = "surya" in myDict # To check weither the item is in dictinay or not
print(val)

# To list out all the keys in a dictonary
print(myDict.keys())

# To list out all the values in a dictonary
values = myDict.values()
print(values)
