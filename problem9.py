#A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
#
#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

#math
#a + b + c = 1000
#a^2 + b^2 = c^2
#
#c = sqrt(a^2 + b^2)
#
#a + b + sqrt(a^2 + b^2) = 1000
#
#a = 1000 - b - c
#
#(1000 - b - c) * (1000 - b - c) + b*b = c*c
#
#10^6 - 1000b - 1000 c - 1000b + b*b + bc -1000c + cb + c*c + b*b = c*c
#
#10^6 - 1000b - 1000 c - 1000b + b*b + bc -1000c + cb + b*b = 0
#
#10^6 - 2000b - 2000c + 2bc + 2b*b = 0

for a in xrange(1,1000):
    for b in xrange(1,1000):
        c = 1000 - a - b
        if(c > 0 and (a*a + b*b) == c*c):
                print "a:%d, b:%d, c:%d, a*b*c=%d" % (a,b,c,a*b*c)
