n = int(input("Enter no of rows you want to print:"))

print("\nPattern 1: \n")

for i in range(n):
    for j in range(i+1):
         print("*",end=" ")
    print()


print("\nPattern 2: \n")

for i in range(n):
    for j in range(n,i,-1):
        print("*",end=" ")
    print()

print("\nPattern 3: \n")

for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(n-1,i,-1):
        print("*",end=" ")
    print()

print("\nPattern 4: \n")

for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for k in range(n,i,-1):
        print("*",end=" ")
    print()

print("\nPattern 5:\n")

for i in range(n):
    for j in range(n-1,i,-1):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()

print("\nPattern 6:\n")

for i in range(n):
    for j in range(i):
        print(" ",end="")
    for k in range(n,i,-1):
        print("*",end=" ")
    print()


print("\nPattern 7:\n")

for i in range(n):
    for j in range(n-1,i,-1):
        print("",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()


print("\nPattern 8:\n")

for i in range(n):
    for j in range(n-1,i,-1):
        print(" ", end=" ")
    for k in range(i):
        print("*",end=' ')
    for l in range(i+1):
            print("*",end=" ")
    print()











