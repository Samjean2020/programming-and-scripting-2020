# Jean Bonsenge
# This program calculates an individual's Body Mass Index (BMI).
# The inputs are the person's height in Centimetres, and weight in Kilograms.
# The output is the weight divided by height in metres squared.

import math

weight = float ( input ( " Enter weight : "))
height = float ( input ( " Enter height : "))

heightSquared = (height/100) ** 2

bmi = weight / heightSquared

print ("BMI is", bmi)




