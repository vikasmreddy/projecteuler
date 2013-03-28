#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
#What is the 10001st prime number?

primes = [2]
prime_index = 1
cur_num = 3

while(prime_index != 10001):
    cur_num_is_prime = True
    for prime in primes:
        if(cur_num % prime == 0):
            cur_num_is_prime = False
            break
    if(cur_num_is_prime):
        primes.append(cur_num)
        prime_index += 1
    cur_num += 1
    
print "10001st prime is: " + str(primes[10000])