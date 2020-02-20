# Jean Bonsenge
# This program outputs whether or not today is a weekday.
weekdays = (" Monday " , 
            " Tuesday " ,
            " Wednesday ", 
            " Thursday " ,
            " Friday " ,
            " Saturday " ,
            " Sunday " )

weekday = weekdays [ 2 : 4 ]
for weekday in weekdays :
    print (weekday)

print (" Are you available for a meeting today? ")
print (" Yes, unfortunately it is weekday.")

weekend = weekdays [ 4 : 6 ]
for weekend in weekdays :
    print (weekend)
print (" Are you available for a picnic today? ")
print (" It is the weekend, Yay! ") 
