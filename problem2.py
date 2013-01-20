num1 = 1
num2 = 2
curnum = 0
sum = 0

while(curnum <= 4000000):
    curnum = num2 + num1
    num1 = num2
    num2 = curnum
    if(curnum % 2 == 0):
        sum += curnum
    
print sum + 2 #adding 2 to account for the very first number
