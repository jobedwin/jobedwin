#  Sum or difference to product

cosa=int(input("Enter the value for cosa :"))
cosb=int(input("Enter the value for cosb :"))
cosc=int(input("Enter the value for cosc :"))

import math

RHS= 2*math.cos(cosa+cosb)/2 * math.cos(cosa-cosb)/2 - math.cos(cosc)

print(RHS)
