# Jean Bonsenge

# This program outputs whether or not today is a weekday.
# This program is ruuning on a Saturday.

import datetime

days = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4: "Friday", 5:"Saturday", 6:"Sunday"}

def dayNameFromWeekday(weekday):
    if weekday > 5:
        print("error")
        return" no running of the program today."

    if weekday < 5:

        print("error")
        return" no running of the program today."
    return days[weekday]

nb = int(input("Enter weekday number: "))

print('\n')

print(dayNameFromWeekday(nb) + (": It is the weekend, yay!")) 

"""I found part of the above code at https://rextester.com/OPSU70132"""


