"""
Purpose - Nature of a number.

Author - Nishant Kumar Ojha

Date - 11 December 2019

"""

#User enters the number

number = int(input("Enter the Number: "))


#Checking the number

if number < 0:
   print("The Number is NEGATIVE.")

elif number > 0:
   print("The Number is POSITIVE.")

elif number == 0:
   print("The Number is ZERO.")

else:
   print("Then Number is not a Number.")