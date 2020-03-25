# Jean Bonsenge
# This program takes a positive floating-point number as input
# and outputs an approximation of its square root.

""" Solve f(x) = x ˄ 2 - y = 0 for x """
""" Newton's method: Iterates new_x = x """
""" Note that f '(x) = 2 x. Thus new_x = x - f(x) / f'(x) """

y = float (input("Enter a positive number: "))
prevx = -1.0
x = 1.0
while abs(x - prevx) > 1e-10:
    prevx = x
    x = x - (x * x - y) / (2 * x)

print('The square root of' , y , 'is approx.' , x )

""" I found part of above Newton's method for square roots from stackoverflow.com at 
https://stackoverflow.com/questions/32291218/use-newtons-method-to-find-square-root-of-a-number"



