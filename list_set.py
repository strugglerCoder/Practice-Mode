n = int(input())
lst=[]
for i in range(n):
    lst.append(input())

myset = set(lst)
print(myset)

print (myset.__len__())

