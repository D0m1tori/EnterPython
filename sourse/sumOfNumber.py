print("If you want stop print 'stop'")
a = input("Enter your number: ")
sumOfPositiveNums = 0
sumOfNegativeNums = 0
while(a != "stop"):
    if(int(a) > 0):
        sumOfPositiveNums += int(a)
    if(int(a) < 0):
        sumOfNegativeNums += int(a)
    a = input("Enter your number: ")
print("Sum of positive nums: ", end="")    
print(sumOfPositiveNums)
print("Sum of negative nums: ", end="")  
print(sumOfNegativeNums)