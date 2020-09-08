# [10,20,30,40] => 10+20+30+40=100

def Sum(list):
    sumVar =0
    for i in list:
        sumVar = sumVar + i
    return sumVar

print(Sum([10,20,30,40]))