a = input()
sumOfPositiveNums = 0
sumOfNegativeNums = 0
print(a)
while(a != "stop"):
    if(int(a) > 0):
        sumOfPositiveNums += int(a)
    if(int(a) < 0):
        sumOfNegativeNums += int(a)
    a = input()
        
print(sumOfPositiveNums)
print(sumOfNegativeNums)