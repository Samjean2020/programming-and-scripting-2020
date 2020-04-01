# Jean Bonsenge
# This program asks the user to input any positive integer
# and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and,
# if it is even, divide it by two, but if it is odd, multiply it by three and add one. 
# Have the program end if the current value is one. 

# input a whole number value
y = int (input(" Enter any positive integer number: "))
# divide to segregate even (modulus with remainder 0) and odd numbers (with the remainder 1).
z = 2
# a while loop is deployed to loop over until set of Boolean conditions are met.
while y > 1:
   if y % z == 0:
       y = y/2
       print(y)
   else:
       y = y * 3 + 1
       print(y)
      
# execute print() function
print()




   
