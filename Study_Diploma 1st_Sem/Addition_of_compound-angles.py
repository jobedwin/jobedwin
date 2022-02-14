#  Addition of compound angles

sinA= int(input("Enter the value of sa : "))
sinB= int(input("Enter the value of sb : "))
cosA= int(input("Enter the value of ca : "))
cosB= int(input("Enter the value of cb : "))

import math
f= math.sin(sinA)*math.cos(cosB) + math.cos(cosA)*math.sin(sinB)

print(f)


cosA= int(input("Enter the value of ca : "))
cosB= int(input("Enter the value of cb : "))
sinA= int(input("Enter the value of sa : "))
sinB= int(input("Enter the value of sb : "))

import math
f= math.cos(cosA)*math.cos(cosB) - math.sin(sinA)*math.sin(sinB)

print(f)