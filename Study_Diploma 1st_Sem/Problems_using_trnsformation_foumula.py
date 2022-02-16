#  Problems on transformatoin formula

cosc= int(input("Enter the number for cosc : "))
cosd= int(input("Enter the number for cosd : "))

import math

f= math.cos((cosc+cosd)/2)*math.cos((cosc-cosd)/2)

print(f)
