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