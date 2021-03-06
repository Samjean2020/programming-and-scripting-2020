                                                Jean Bonsenge

                                        Programming and Scripting 2020 

                                                Repository Purpose

Record and present weekly tasks required by the HDip. in Science in Computing (Data Analytics) Programming and Scripting Module for January to June 2020 Semester.

                                                Repository Content

Topic 1: Programming in Python

Weekly task 1: running a small program, hello.py and goodbye.py

Topic 2: Statement

Weekly task 2: write a program that calculates somebody’s BMI (Body Mass Index)…, bmi.py

Topic 3: State

Weekly task 3: write a program that takes asks a user to input and outputs every second letter in reverse order... secondstring.py

Topic 4: Controlling the flow

Weekly task 4: write a program that asks the user to input any positive integer and outputs the successive values…, collatz.py

Topic 5: Data

Weekly task 5: write a program that outputs whether or not today is a weekday…weekday.py

Topic 6: Functions

Weekly task 6: write a program that takes a positive floating-point number as an input and outputs an approximation of its square root, squareroot.py

Topic 7: Files

Weekly task 7: write a program that reads in a text and outputs the number of e’s it contains…es.py moby-dick.txt

Topic 8: Looking ahead. Matplotlib.pyplot

Weekly task 8: write a program that displays a plot of the functions f(x) = x, g(x) = x2 and h(x) = x3 in the range of [0, 4] on the one set of axes, plot.py

                                                Instructions on how to run the files
                                                
Python 3x programming language codes are used for the writing of the above weekly tasks. Visual Studio Code (VSC), Cmder, IPython, IPython log file, Notepad++ are text-editors used for this purpose. The programs can be run under  VSC terminal, Cmder, IPython, etc. command lines and cloned to a repository if necessary. For the purpose of this assignment, files are cloned to this repository (programming-and-scripting-2020) via the following URL address: https://github.com/Samjean2020/programming-and-scripting-2020.git using relevant git commands, namely: git init, git clone, git add  . , git commit –m (“comments”), and git push or git pull. Upload files option available at GitHub was also used.


                                                Documentation     

                                          Description of solutions

                    Weekly task 1: running a small program, hello.py and goodbye.py
A single-line code in python is enough to provide specific instructions to be executed on a machine with an Operating System (OS): Microsoft Disk Operating System (MS-DOS), UNIX OS, and LINUX OS. The call of the print() function, displays the output of the string-type of data: Hello, World for the file hello.py and Goodbye, World regarding the file goodbye.py

                    Weekly task 2: write a program that calculates somebody’s BMI (Body Mass Index). The inputs are the person's height                     in centimetres, and weight in kilograms. The output is the weight divided by height in metres squared.

1. Call a module to perform mathematical functions. 
2. Provide float numbers as inputs for both weight and height.
3. Have height squared.
4. Solve the problem.
5. Execute print()function.
6. Exit

Source code at: https://www.w3resource.com/python-exercises/python-basic-exercise-66.php
Source code at: https://docs.python.org/3/library/math.html



                    Weekly task 3: write a program that takes asks a user to input and outputs every second letter in reverse order, secondstring.py

1. Provide a text sequence type: string. 
2. Use the built-in function len() function to obtain the length of the string (:44). 
3. Start from end of the string and output every second letter.
4. Execute print() function. 
5. Exit.

Source: https://www.w3schools.com/python/ref_func_len.asp



                  Weekly task 4: write a program that asks the user to input any positive integer and outputs the successive values of                     the following calculation. At each step calculate the next value by taking the current value and, if it is even,                         divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is                       one. collatz.py  

1. Input a whole number value.
2. Set a divide to segregate even (modulus with remainder 0) and odd numbers (with the remainder 1).
3. Deploy a while loop to loop over,the block, until the set Boolean conditions are met.
4. Execute print()function.
5. Exit.
Source: A Whirlwind Tour of Python, p.37-8 (Control Flow).


                  Weekly task 5: write a program that outputs whether or not today is a weekday…weekday.py
                  An example of running this program on a Thursday is given below... 
                  An example of running this program on a Saturday is as follows...

1. Import Python's datetime module
2. Make array (a dictionary) of all the days in order.
3. Have indexed array items starting at 0 to Monday, ending with 6 to Sunday.
4. Define a function for weekday and set up an if loop,to loop over until the set Boolean conditions are completed.
5. Get keyboard input, but convert it to integer.
6. Print the results of the function.
7. Exit
Sources: https://rextester.com/OPSU70132
and : https://pythontic.com/datetime/date/weekday

Source: at https://rextester.com/OPSU70132

Note: Comments on code for weekday.py file(running this program on a Thursday) apply to the file: weekday2.py, whereby an example of running this program on a Saturday is used. This is the same for the above descritption of solution.

                Weekly task 6: write a program that takes a positive floating-point number as an input and 
                outputs an approximation of its square root. squareroot.py

1. Enter a positive floating-point number.
2. Iteration under a while loop as per Newton's Method.
3. Display an approximation square root of the floating-point number.

Source: Newton's method for square roots from stackoverflow.com at
https://stackoverflow.com/questions/32291218/use-newtons-method-to-find-square-root-of-a-number"
 

                    Weekly task 7: write a program that reads in a text and outputs the number of e’s it contains…es.py moby-dick.txt

1.Take the file name and the letter to be counted from the user.
2. Read each line from the file and split the line to form a list of words.
3. Use a for loop to traverse through the words in the list and another for loop to traverse through the letters in the word.
4. Check if the letter provided by the user and the letter encountered over iteration is equal and if they are, increment the letter count.
5. Exit.

Source: Python Program that Reads a Text File and Counts the Number of Times a Certain Letter Appears in the Text File
https://www.sanfoundry.com/python-problems-solutions/

Please see comments on code for this weekly task under the filename: es.py moby-dick.txt

                  Weekly task 8: write a program that displays a plot of the functions f(x) = x, g(x) = x2 and h(x) = x3 in the range of [0, 4] on the one set of axes, plot.py

1. Import numpy and matplotlib.pyplot to deal with numbers and plots,respectively. 
2. Describe functions for plotting.
3. Make a variable and assign values in floating-point precision type, and in one time on x-axis.
4. Have values on y-axis squared. 
5. Have values on y-axis to the third power or cube.
6. Display the title of the plot and labels of functions.
7. Use the plot() command and display the plot itself.
Source: https://matplotlib.org/tutorials/introductory/pyplot.html 





