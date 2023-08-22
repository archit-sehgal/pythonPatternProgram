num=int(input("enter the no. for stars: "))
for x in range(0,num+1):
    for j in range(num-x):
        print(" ",end="")
    for i in range(x+1):
        print("*",end=" ")
    print()
for x in range(0,num):
    for j in range(x+1):
        print(" ",end="")
    for i in range(num-x):
        print("*",end=" ")
    print()