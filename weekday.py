# This program outputs whether or not today is a weekday.
import calendar

D=dict(enumerate (calendar.day_name))

print ('Are you available for a meeting today?')
print (calendar.day_name[3])
print('Yes, unfortunately it is weekday.')

print ('Are you available for a picnic today?')
print (calendar.day_name[5])
print ('It is the weekend, Yay!')


