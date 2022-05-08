#  To represent a pair of a straight line

a= int(input("Entre the number for a :"))
h= int(input("Entre the number for h:"))
b= int(input("Entre the number for b :"))
g= int(input("Entre the number for g :"))
f= int(input("Entre the number for f :"))
c= int(input("Entre the number for c :"))

x = a*1*(b*c-f*f)

print (x)

y = h*-1*(h*c-g*f)

print (y)

z = g*1*(h*f-g*b)

print (z)

S= x+y+z

if S == 0:
    print (" The equation represents a pair of straight line")

else:
     print ("The equation does not represents a pair of straight line")

