# To convert the whole string to upper case 
a = "surya is a developer"
b=a.upper()
print(b)

# To replace a specific sub-stringin a string with another string
b = a.replace("surya","teja")
print(b)

# To find a specific substring in the string
# It retruns the starting index value of the sub-string
print(a.find("developer"))

# If the sub-string is not found then it returns -1
print(a.find("cat"))


print("0123456".find('1'))
name = 'Lizz'
print(name[0:2])
var = '01234567'
print(var[::2])
