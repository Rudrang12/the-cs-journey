# -------------PROBLEM SET_0-----------#
 
#GOAL-->To write a python code which takes two numbers as user inputs,
#       x and y, and performs the following operations-
#           1.x^y [i.e. x raised to the power y]
#           2.log(base2) of x 
#         

import numpy    # Importing the module numpy


x = int(input("enter a number: "))    #Taking the user's input for a number x in an integeral form

y = int(input("enter a number: "))    #Taking the user's input for a number y in an integeral form



print("x^y is", x**y)    #Printing the result of the operation x**y [i.e. x raised to the power y]

print("log(base2) of x is:",numpy.log2(x))   #Printing the result of the operation log(base2) of x