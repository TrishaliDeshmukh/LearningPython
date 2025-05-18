#String Formatting
#Inserting strings within a string
String = "I Like %s " % "Python"
print(String)

#Inserting integers within a string
temp="Programming"
String2 = "I like %s" % temp
print(String2)

#Inserting floats within a string
String3 = "I like %s and %s " %("Python",temp)
print(String3)

my_string = "%i + %i = %i" %(1,2,3)
print(my_string)

String4 = "%f" % (1.11)
print(String4)

String5 = "%.2f" %(1.11)
print(String5)

String6 = "%.2f" %(1.17)
print(String6)