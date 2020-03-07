# Jean Bonsenge
# This program reads in a text file and outputs
# the number of e's it contains.
# This program should take the filename from an argument on the command line.

filename = input ("Enter file name: ")
# I changed the filename ( $ python es.py moby-dick.text) taken from an initial argument
# on the command line to (reades.py), because under the filename ($ python es.py moby-dick.text)
# this program outputs (0) on the occurences of e's  within the Moby-Dick text.

l=input ("Enter letter to be searched: ")
m = 0

with open ('reades.py') as f:
        for line in f:
            words = line.split ()
            for i in words:
                for letter in i:
                    if(letter==l):
                        m=m+1
print("occurences of the letter: ")
print(m)
# I found the above code online: https://www.sanfoundry.com/python-program-read-file-counts-number/

