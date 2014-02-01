max_length = 0
max_n = -1
cache = { }
for n in xrange(2, 1000000):
    cur = n
    length = 0
    print "*** chain start for: " + str(cur)
    while cur != 1:
        if cache.get(cur) != None:
            length += cache[cur]
            print "chain cache found for: " + str(cur) + " with length: " + str(cache[cur])
            break
        if cur % 2 == 0:
            cur = cur / 2
        else:
            cur = 3*cur + 1
        length += 1
        print "chain continue: " + str(cur)
    
    if cache.get(n) is not None:
        raise Exception("WTF")
    else:
        cache[n] = length
    
    length += 1 #adding 1 to account for the number 1 in the chain
    
    print "*** chain finished, length is: " + str(length)
    if length > max_length:
        max_length = length
        max_n = n

print max_n