#  To find HCF of any two numbers
num1=int(input("Enter 1st Number :"))
num2=int(input("Enter 2nd Number :"))
def compute_hcf(x, y):
     if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

x = num1
y = num2

print("The H.C.F. is", compute_hcf(num1, num2))