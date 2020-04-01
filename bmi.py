# Jean Bonsenge
# This program calculates an individual's Body Mass Index (BMI).
# The inputs are the person's height in centimetres, and weight in kilograms.
# The output is the weight divided by height in metres squared.

# Call a module to perform mathematical functions. 
import math
# Provide float numbers as inputs for both weight and height as specified above.
weight = float ( input ("Enter weight : "))
height = float ( input ("Enter height : "))
# Use the formula below to find height squared.
heightSquared = (height/100) ** 2
# Apply the formula below to solve this problem.
bmi = weight / heightSquared

# Execute print() function.
print ("BMI is", bmi)

# I found part of this code at:
# https://www.w3resource.com/python-exercises/python-basic-exercise-66.php
# , and https://docs.python.org/3/library/math.html






