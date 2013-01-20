import math

num = 600851475143
max_possible_factor = int(math.ceil(num/2.0))
min_possible_factor = 2
i = min_possible_factor
max_prime_found = -1

while(i <= max_possible_factor):
    #check if i is a factor of num
    #print "checking: " + str(i)
    if(num % i == 0):
        #check if i is prime
        max_possible_factor = num / i
        print str(i) + " is a factor, adjusting max possible factor to: " + str(max_possible_factor)
        i_is_prime = True
        largest_possible = int(math.ceil(i/2.0))
        for g in range(2, largest_possible + 1):
            if(i % g == 0):
                print str(i) + " is not prime"
                i_is_prime = False
                break
        if(i_is_prime):
            print str(i) + " is prime"
            max_prime_found = i
    i += 1    

print "max prime factor is: " + str(max_prime_found)
