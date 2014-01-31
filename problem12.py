triangle_num = 1
num_on = 2

while True:
    num_divisors = 0
    cur = 1
    #print "checking %d" % (triangle_num,)
    end = triangle_num
    while True:
        if triangle_num % cur == 0:
            num_divisors += 2
            end = (triangle_num / cur) - 1
        cur +=1
        if cur > end:
            break

    if num_divisors > 500:
        print "triangle_num: %d, divisors: %d" % (triangle_num, num_divisors)
        break
    
    triangle_num += num_on
    num_on += 1