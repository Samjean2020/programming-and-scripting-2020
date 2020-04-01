# Jean Bonsenge

# This program outputs whether or not today is a weekday.
# An example of running this program on a Thursday is given below. 

# import Python's datetime module
import datetime

# Make array (a dictionary) of all the days in order.
# Have indexed array items starting at 0 to Monday, ending with 6 to Sunday.
days = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4: "Friday", 5:"Saturday", 6:"Sunday"}

# Define a function for weekday and set up an if loop, 
# to loop over until the set Boolean conditions are completed.
def dayNameFromWeekday(weekday):
    if weekday > 3:
        print("error")
        return" no running of the program today."

    if weekday < 3:

        print("error")
        return" no running of the program today."
    return days[weekday]

# Get keyboard input, but convert it to integer.
nb = int(input("Enter weekday number: "))
print('\n')

# Print the results of the function
print(dayNameFromWeekday(nb) + (": Yes, unfortunately today is a weekday.")) 

"""I found part of the above code at https://rextester.com/OPSU70132"""
"""and at: https://pythontic.com/datetime/date/weekday"""







