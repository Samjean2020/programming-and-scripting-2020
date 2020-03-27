# This program outputs whether or not today is a weekday.

import datetime

days = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4: "Friday", 5:"Saturday", 6:"Sunday"}

def dayNameFromWeekday(weekday):
    if weekday > 4:
        print("error")
        return" an unknown day"
    return days[weekday]

nb = int(input("Enter weekday number [0-4]: "))
print('\n')

print("Yes, unfortunately today is a weekday.")

"""I found part of above code at https://rextester.com/OPSU70132"""






