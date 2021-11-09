#  LCM  of any two numbers
print("Enter 2 Numbers: ")
num1 = int(input())
num2 = int(input())

if num1>num2:
    lcm = num1
else:
    lcm = num2

while True:
    if lcm%num1==0 and lcm%num2==0:
        break
    else:
        lcm = lcm + 1

print("LCM of two numbers is =")