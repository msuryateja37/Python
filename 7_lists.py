# Lists are also ordered sequences and are mutable too
# here is an example
l = ["Michael Jackson", 10.1, 1982]
print(l)
print(type(l))

# Mutability
l[0] = "Surya"
print(l)

# nesting
my_list = ["Surya", 10.1, 1982, [1,2],(1,2)]
print(my_list)
print(my_list[4][0])
print(my_list[-1])
print(len(my_list))

# We can add elements to the same list
my_list.extend(["pop", 20])
print(my_list)

#similarly this adds elements to the list but in nested form
my_list.append(["new",52])
print(my_list)
# Single element is also treated as nested for append method
my_list.append([25])
print(my_list)

# we can delete specific elements in list since lists are mutable
del(my_list[5])
print(my_list)

# We can convert a String to list using split
a = "my name is surya"
b = a.split()
print(b)

# We can make list by sperating the string on a specific character (aka delimiter)
c = "a,b,c,d".split(",")
print(c)

# List Aliasing
A = ["banana",10.2,54]
B = A
B[0] = "tomato"
print(A)
# It is a side effect of aliasing as 'A' and 'B' are referencing to the same list.
# Therefore if we change elements of one variable it impacts the other referencing the same.
# To avoid such issues we do
# List Cloning
A = [1,2,3,4,5,6]
B = A[:]
print(A)
print(B)
# Now both the variables are referencing to two diffrent lists.
# Changes made in one will not be reflected to another in any way.

# To get more information on any object in python
help(A)
