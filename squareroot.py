# Jean Bonsenge
# This program takes a positive floating-point number as input
# and outputs an approximation of its square root.

# Enter a positive floating-point number.
y = float (input("Enter a positive number: "))
prevx = -1.0
x = 1.0

# Iteration under a while loop as per Newton's Method.
while abs(x - prevx) > 1e-10:
    prevx = x
    x = x - (x * x - y) / (2 * x)
    
# Display an approximation square root of the floating-point number.
print('The square root of' , y , 'is approx.' , x )

""" I found part of the above Newton's method for square roots from stackoverflow.com at 
https://stackoverflow.com/questions/32291218/use-newtons-method-to-find-square-root-of-a-number"""



