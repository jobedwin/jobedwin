#  A number is divisible by 10 only when its unit digit is 0.
num=int(input("Enter your number :"))
x=[int (a) for a in str(num)]
s = str(x[-1])
print ("unit digit is", s)
if (int(s) % 10 ==0):
    print("is divisible by 10")
else :
    print ("is not divisible by 10")