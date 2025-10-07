i=0
while(i<5):
    j=0
    while(j<5):
        if i==0 or j==4 or i==2 or j==0 and i<=2:print("*",end=" ")
        else:print(" ",end=" ")
        j=j+1
    print(end=" ")

    j=0
    while(j<5):
        if i==0 or i==4 or i==2 or j==4 or j==0 and i<=2:print("*",end=" ")
        else:print(" ",end=" ")
        j=j+1
    print(end=" ")
    j=0
    while(j<5):
        if i==0 or j==0 or j==4 or i==4:print("*",end=" ")
        else:print(" ",end=" ")
        j=j+1
    print(end=" ")
    j=0
    while(j<5):
        if i==0 or j==0 or j==4 or i==4:print("*",end=" ")
        else:print(" ",end=" ")
        j=j+1
    print()
    i+=1
