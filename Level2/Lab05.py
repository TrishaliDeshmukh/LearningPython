#Take input from a user and print the table

n=int(input("Enter the number for which you want the Table: "))
i=1
for i in range (1,11) :
    print(f"{n}*{i}={i*n}")

