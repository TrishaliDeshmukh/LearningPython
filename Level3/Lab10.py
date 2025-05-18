#StringImmutability
string = "I am Immutable"
#string[0] = '0' # Will give error

# With ID method
str1 = "Python"
print(id(str1))
str1 = "Learning"
print(id(str1))

val = None
print(val)  # prints "None" and returns None
print(type(val))