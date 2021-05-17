# strings in python

#storing a string in variable and displaying its type
x = "my name"
print(x,"\n",type(x))

# we can declare strings by 2 types

# first using double quotes 
x="this is a string"
print(x)

# second using single quotes
x='this is also a string'
print(x)

# numbers inside the quotes are considered as string
x="123465798"
print(x)

# special characters inside the quotes are also considered as strings
x='!@#$%^&*()'
print(x)

# strings are ordred form of characters therefore strings can be accessed via index number
x= "hello surya"
print(x[4])

# also we can access the characters in a specific range
print(x[2:6])

# we can access the string elements in reverse order without actually reversing the string
# By using negative numbers we can access from the rear side of the string
print(x[-1])
print(x[-6:-2])

# This prints the every second letter of the string
print(x[::2])

# This prints the every second letter in the following range
print(x[2:4:2])

# This returns the length of the string
print(len(x))
