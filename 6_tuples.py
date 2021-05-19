# Tuples and list are compound data types and are one of the key types of data structures in python.
# Example
my_tuple = (10,5,8,9,7,5,6,2,3,1,4)
print("example of a tuple")
print(my_tuple)

# In python all variables can be contained in a tuple and its data type is tuple
a = ("surya",10,10.0)
print(a)

# type tuple
print(type(a))

# elements in a tuple can be accessed using index value of each element
print(a[2]) # prints 10.0

#print(a[5]) # this prints error
#IndexError: tuple index out of range

# We can use negative index which starts from the rear end
print(a[-1]) # prints 10.0

# we can concatinate two or more tuples
b = a+my_tuple
print(b)

# Tuples are immutable
# a[0]="hello"
# It yields following error: TypeError: 'tuple' object does not support item assignment

# To print a sorted tuple
print(sorted(my_tuple))

# Tuples nesting
a=(1,2,("hello",10,'surya'),(2,"number"))
print(a)
print(a[2][0]) # accessing the nested tuples elements


