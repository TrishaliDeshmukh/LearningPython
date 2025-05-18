# Indexing and Reverse Indexing
#A string in Python is indexed from 0 to n-1 where n is its length
batman = "Bruce Wayne"
first = batman[0]  # Accessing the first character
print("the first character: ",first)
space = batman[5]  # Accessing the empty space in the string
print("Accessing the empty space in the string:",space)
last = batman[len(batman) - 1]
print(last)

# The following will produce an error since the index is out of bounds
print("Length of batman is:",len(batman))
batman = "Bruce Wayne"
print(batman[-1])  # Corresponds to batman[10]
print(batman[-5])  # Corresponds to batman[6]