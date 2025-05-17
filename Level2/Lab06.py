# List the all the functions avaiable for the String Data Type

#printing length of string stored in variable a
a="python"
print("Length of python is: ",len(a))

#Returns a centered string
print(a.center(10,'*'))

#print first letter of string in uppercase
print("First letter of 'python' in uppercase:  ",a.capitalize())


#Searches the string for a specified value and returns the position of where it was found
ab=[1,2,5,8,3]
print("Index position of '3' is: ",ab.index(3))

#print string  in lowercase
b="PYTHON"
print("'PYTHON' in lowercase: ",b.casefold())

c = "How are you ?"
#printing count of letter available in string
print("Letters present in 'python' is: ",c.count('o'))

#Returns true if the string ends with the specified value
print("'?' is present in 'How are you ?' :",c.endswith('?'))

#Searches the string for a specified value and returns the position of where it was found
print("'are' is present at what position :",c.find("are"))

d = "Sunday, {}"
#Formats specified values in a string
print("Formating string: ",d.format('Funday'))
e='Hello, {name}'
print(e.format_map({'name':'World'}))

#Returns True if all characters in the string are alphanumeric
bool="apple23"
print("True if all characters in the string are alphanumeric: ",bool.isalnum())

