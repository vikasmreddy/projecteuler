#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
#Find the sum of all the primes below two million.

import math

primes = [2]
prime_sum = 2
cur_num = 3

while(cur_num < 10000):
    cur_num_is_prime = True
    
    i = 2
    while(i < cur_num / 2 + 1):
        if(cur_num % i == 0):
            cur_num_is_prime = False
            break    
        i += 1
    
    if(cur_num_is_prime):
        #print "prime: " + str(cur_num)
        prime_sum += cur_num 
    cur_num += 1
    
print "sum is : " + str(prime_sum)