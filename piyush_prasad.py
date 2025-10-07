for i in range(0,5):
    for j in range(0,5):
        if i==0  or j==0 or i==2 or (j==4 and i<=2):print("*",end=" ")
        else:print(" ",end=" ")
    print(end=" ")

    for j in range(0,5):
        if i==0 or i==4 or j==2:print("*",end=" ")
        else:print(" ",end=" ")

    print(end=" ")
    for j in range(0,5):
        if i==j and i<=2 or i+j==5-1 and i<=2 or j==2 and i>=2:print("*",end=" ")
        else:print(" ",end=" ")

    print(end=" ")
    for j in range(0,5):
        if j==0 or i==4 or j==4:print("*",end=" ")
        else:print(" ",end=" ")
    print(end=" ")
    for j in range(0,5):
        if i==0 or i==2 or i==4 or j==4 and i>=2 or j==0 and i<=2:print("*",end=" ")
        else:print(" ",end=" ")
    print(end=" ")
    for j in range(0,5):
        if i==2 or j==0 or j==4:print("*",end=" ")
        else:print(" ",end=" ")

    print(end="     ")
    for j in range(0,5):
        if i==0 or j==0 or i==2 or j==4 and i<=5//2:print("*",end=" ")
        else:print(" ",end=" ")
    print(end=" ")
    for j in range(0,5):
        if i==0 or j==0 or i==2 or j==4 and i<=2 or j==i and i>=2:print("*",end=" ")
        else:print(" ",end=" ")
    print(end=" ")
    for j in range(0,5):
        if i==0 or j==0 or i==2 or j==4:print("*",end=" ")
        else:print(" ",end=" ")
    print(end=" ")
    for j in range(0,5):
        if i==0 or i==4 or j==0 and i<=2 or j==4 and i>=2 or i==2:print("*",end=" ")
        else:print(" ",end=" ")
    print(end=" ")
    for j in range(0,5):
        if i==0 or j==0 or i==2 or j==4:print("*",end=" ")
        else:print(" ",end=" ")
    print(end=" ")
    for j in range(0,5):
        if i==0 or j==0 or i==4 or j==4:print("*",end=" ")
        else:print(" ",end=" ")
    print()
    
