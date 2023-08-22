num=int(input("enter a no:"))
for x in range(0,num+1):
    for j in range(num-x):
        print(" ",end=" ")
    for y in range(x+1):
        print("*",end=" ")
    print()
for x in range(0,num):
    for j in range(x+1):
        print(" ",end=" ")
    for y in range(num-x):
        print("*",end=" ")
    print()