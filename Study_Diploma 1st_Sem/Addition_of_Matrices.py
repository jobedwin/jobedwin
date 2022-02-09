#  Two or more matrices of same order can be added by adding the elements in their corresponding positions

row = int(input("enter the row number:"))
column = int(input("enter the column number:"))


print("enter the elemnts for matrix1:")
matrix1 = [[int(input()) for i in range (column)] for j in range (row)]
print("matrix1:")
for i in range(row):
    for j in range (column):
        print(format(matrix1[i] [j], "<3") ,end="")
    print()

print("enter the elemnts for matrix2:")
matrix2 = [[int(input()) for i in range (column)] for j in range (row)]
print("matrix2:")
for i in range(row):
    for j in range (column):
        print(format(matrix2[i] [j], "<3") ,end="")
    print()


result = [[0 for i in range (column)] for j in range (row)]
for i in range(row):
    for j in range(column):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

print("result is:2")
for i in range(row):
    for j in range(column):
        print(format(result[i][j],"<3") ,end="")
    print()