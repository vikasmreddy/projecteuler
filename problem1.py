# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

max_num = 1000

sum = 0
five_iterator = 5
three_iterator = 3

while(three_iterator < max_num or five_iterator < max_num):
    while(three_iterator < five_iterator):
        print "three_iterator: adding in " + str(three_iterator)
        sum += three_iterator
        three_iterator += 3
        print "three_iterator: " + str(three_iterator)
        
    if(three_iterator == five_iterator):
        three_iterator += 3
    
    if(five_iterator < max_num):
        print "five_iterator: adding in " + str(five_iterator)
        sum += five_iterator
        five_iterator += 5
        print "five_iterator: " + str(five_iterator)
    
print sum
    
    
