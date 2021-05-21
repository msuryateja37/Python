# Let’s cover sets; they are also a type of collection.
# Sets are a type of collection. This means that like lists and tuples, you
# can input different python types. Unlike lists and tuples they are unordered.
# This means sets do not record element position. Sets only have unique elements.
# This means there is only one of a particular element in a set.

mySet = {"rock","paper","sissors","rock","surya"} # Creating a set
print(mySet)

# We get the output diffrent at each run

# Converting a list to set
myList = [10,20,30,52,"surya","teja"]
print(type(myList))
print(myList)
myList = set(myList) # we provide a list as argument to set method
print(type(myList))
print(myList)

# Using the same way we can change a tuple to set too
myList = (10,20,30,52,"surya","teja")
print(type(myList))
print(myList)
myList = set(myList) # we provide a list as argument to set method
print(type(myList))
print(myList)


# Now lets go for Set Operations
myList.add("rock")
print(myList)
myList.remove("surya")
print(myList)

print("teja" in myList) # returns True because the set contains the argument 
print("surya" in myList) # returns False because the set does not contains the argument

mySetOne = {1,2,3,4,5,6}
mySetTwo = {4,5,9,8,7}
newSet = mySetOne & mySetTwo # Set Intersection
print(newSet)\
               
unionSet = mySetOne.union(mySetTwo) #Set Union
print(unionSet)

mySubset = mySetOne.issubset(mySetTwo) # Check for subset
print(type(mySubset))
print(mySubset)

