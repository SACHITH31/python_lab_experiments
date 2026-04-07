# Matrix A
A = [[1, 2],[3, 4]]

# Matrix B
B = [[5, 6], [7, 8]]

# Addition
add = []
for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])
    add.append(row)
print("Addition:", add)

# Transpose of A
transpose = []
for i in range(len(A[0])):
    row = []
    for j in range(len(A)):
        row.append(A[j][i])
    transpose.append(row)
print("Transpose of A:", transpose)

# Multiplication
mul = []
for i in range(len(A)):
    row = []
    for j in range(len(B[0])):
        sum = 0
        for k in range(len(B)):
            sum += A[i][k] * B[k][j]
        row.append(sum)
    mul.append(row)
print("Multiplication:", mul)