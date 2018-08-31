import sys
import random
terms = sys.argv[1].split('d')
total = 0
print "Rolling " + str(terms[0]) + " x " + str(terms[1]) + " sided dice:" 
for i in range(0, int(terms[0])):
    roll = random.randint(1,int(terms[1]))
    print " > " + str(roll)
    total += int(roll)
print "------------------------"
print "TOTAL ROLLED: " + str(total)

