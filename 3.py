num=int(input("enter the no. of stars: "))
for x in range(0,num):
    for j in range(num-x):
        print(" ",end=" ")
    for i in range(x+1):
        print("*",end=" ")
    print()