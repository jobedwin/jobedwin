#  A number is divisible by 2 if its unit digit is any of 0, 2, 4, 6, 8
num=int(input("Enter your number :"))
x=[int (a) for a in str(num)]
y = str(x[-1])
print ("unit digit is", y)
if (int(y) % 2 ==0):
    print("is divisible by 2")
else :
    print ("is not divisible by 2")
