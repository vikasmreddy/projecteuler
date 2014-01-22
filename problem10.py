#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
#Find the sum of all the primes below two million.

from sets import Set

max_num = 2000000
prime_possibilities = Set(xrange(2, max_num-1))

for i in xrange(2, max_num-1):
    multiplier = 2
    multiplied = i * multiplier
    while multiplied < max_num:
        #print "checking %d*%d=%d, len(prime_possibilities)=%d" % (i,multiplier, multiplied,  len(prime_possibilities))
        try:
            prime_possibilities.remove(multiplied)
        except KeyError:
            pass
        multiplier += 1
        multiplied = i * multiplier

sum = 0
for p in prime_possibilities:
    print str(p) + ", "
    sum += p
    
print "Sum of primes below %d is %d" % (max_num, sum)

#max_num = 10001 #148933
#
#prime_sum = 2
#primes = [2] * max_num
#prime_index = 1
#cur_num = 3
#
#while(prime_index != max_num):
#    cur_num_is_prime = True
#    for prime in primes:
#        if(cur_num % prime == 0):
#            cur_num_is_prime = False
#            break
#    if(cur_num_is_prime):
#        primes[prime_index] = cur_num
#        prime_index = prime_index + 1
#        prime_sum = prime_sum + cur_num
#    cur_num = cur_num + 1
#
#print "148933st prime is: %d, sum is %d\n" % (primes[max_num-1],prime_sum)
#
#exit
#
#
#import math
#
#primes = [2]
#prime_sum = 2
#cur_num = 3
#
#while(cur_num < 1000000):
#    cur_num_is_prime = True
#    
#    i = 2
#    while(i < cur_num / 2 + 1):
#        if(cur_num % i == 0):
#            cur_num_is_prime = False
#            break    
#        i += 1
#    
#    if(cur_num_is_prime):
#        #print "prime: " + str(cur_num)
#        prime_sum += cur_num 
#    cur_num += 1
#    
#print "sum is : " + str(prime_sum)