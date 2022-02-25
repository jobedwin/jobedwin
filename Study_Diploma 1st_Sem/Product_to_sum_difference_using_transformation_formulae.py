cosc= int(input("Enter the number for cosc : "))
cosd= int(input("Enter the number for cosd : "))
sinc= int(input("Enter the number for sinc : "))
sind= int(input("Enter the number for sind : "))

import math

cos= math.cos((cosc+cosd)/2)
sin= math.sin((sinc-sind)/2)

print(cos)
print(sin)
