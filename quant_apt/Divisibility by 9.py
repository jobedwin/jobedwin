#  A number is divisible by 9 only when the sum of its digits is divisible by 9
num=int(input ("Enter your number"))
if (num%9==0):
    print("{} is divisible by 9".format(num))
else: 
    print("{} is not divisible by 9".format(num))