# Jean Bonsenge
# This program takes a positive floating-point number as input 
# and outputs an approximation of its square root.

# please enter a positive number: 14.5

import math

pNumber = 14.5

sqrt = (pNumber ** 2 / 2 )

print ( sqrt )

def newtons_method
 ( num, estimate):
 # computing a new_estimate
new_estimate = ( estimate +num / estimate) / 2
print(new_estimate)
#Base case: comparinf our estimate with built-in function value

if new_estimate = = math.sqrt(num):
    return True
else:
    return newtons_method (num, new_estimate)
                          

the 30's squarre root:
result should be () : 5 and 6

news_method (30,5)
number is 30 and root is 5
the result from each recursive calls are:

5.5
5.477...
5.4777
5.4777
the last result is the most accurate computation of the Square root of number.

It is the same value as the built-in function math. sqrt ().
