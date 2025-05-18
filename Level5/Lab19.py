# Boolean literals
x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10
print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)
# Special literal
drink = "Available"
food = None
def menu(x):
 if x == drink:
     print(drink)
 else:
     print(food)
menu(drink)
menu(food)
# Literal Collections
fruits = ["apple", "mango", "orange"] #list
numbers = (1, 2, 3) #tuple
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'}
#dictionary
vowels = {'a', 'e', 'i' , 'o', 'u'} #set
print(fruits)
print(numbers)
print(alphabets)
print(vowels)