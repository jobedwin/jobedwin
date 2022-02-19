#  Product to sum or difference

sinc= int(input("Enter the number for sinc : "))
sind= int(input("Enter the number for sind : "))
cosc= int(input("Enter the number for cosc : "))
cosd= int(input("Enter the number for cosd : "))

import math

sin= math.sin((sinc+sind)/2)
cos= math.cos((cosc-cosd)/2)

print(sin)
print(cos)

