# Jean Bonsenge
# This program asks the user to input any positive integer
# and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and,
# if it is even, divide it by two, but if it is odd, multiply it by three and add one. 
# Have the program end if the current value is one. 
#
# please enter a positive integer: 10

p = int (input ( " please enter a positive integer: ")) 
m = int (input ( " please enter the second integer you want to divide by: "))

answer = int (p / m)

if (p % m) == 0:
    print(p, "divided by", m, "leaves a remainder of zero, therefore the remainder is even.")
    print("I'll be run too if the condition is True.")
if (p % m) != 0:
    print(p, "divided by", m, " leaves a remainder of one, therefore the remainder is odd.")
    print(" I'll be run too even if the condition is False")
    print(p = p * 3) # currentNumber = currentNumber * 3 ( or currentNumber * = 3)
    print(p = p + 1) # currentNumber = currentNumber + 1 ( or currentNumber + = 1)
    print("p")  
while p < 10:
    print(p, end = " ")
    
print("I'll run no matter what.")
print("I'll have the program end if the current value is one")

print("Thank you for running my program.")