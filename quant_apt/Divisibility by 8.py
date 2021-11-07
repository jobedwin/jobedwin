# A number is divisible by 8 if the number formed by hundred's ten's and unit's digit of the given number is divisible by 8
num=int(input("Enter  your number :"))
x=[int (a) for a in str(num)]
print(x)
s = str(x[-3])+str(x[-2])+str(x[-1])
print ("Number formed by hundred's ten's and unit's is", s)
if (int(s) % 8 ==0):
    print("is divisible by 8")
else :
    print ("is not divisible by 8")