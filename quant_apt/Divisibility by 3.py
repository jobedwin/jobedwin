#  A number is divisible by 3 only when the sum of its digits is divisible by 3
num=int(input("Enter your number"))
if(num%3==0):
    print("{} is divisible by 3".format(num))
else:
    print("{} is not divisible by 3".format(num))