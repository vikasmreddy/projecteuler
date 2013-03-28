#The sum of the squares of the first ten natural numbers is,
#
#1^2 + 2^2 + ... + 10^2 = 385
#The square of the sum of the first ten natural numbers is,
#
#(1 + 2 + ... + 10)^2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.
#
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

num_natural_numbers = 100
diff_squareofthesum_sumofthesquares = 0

for i in range(1, num_natural_numbers + 1):
    squareofsum = 0
    for j in range(1, num_natural_numbers + 1):
        squareofsum += i*j
        
    diff_squareofthesum_sumofthesquares += squareofsum - i*i
    
print diff_squareofthesum_sumofthesquares