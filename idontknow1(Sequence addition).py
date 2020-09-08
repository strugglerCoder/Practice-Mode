n = int(input("enter no for sequence addition : "))
ans = 0

if n == 0:
    print(ans)
else:
    for i in range(1,n+1):
        ans = ans+i
    print(ans)

