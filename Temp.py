Q3 A.1 Construct the following matrices without inline
1) Identity matrix of order 10 × 10
identity_matrix = []
for i in range(10):
    row = []
    for j in range(10):
        if i == j:
            row.append(1)
        else:
            row.append(0)
    identity_matrix.append(row)

print("Identity Matrix (10x10):")
for row in identity_matrix:
    print(row)

2) Zero matrix of order 7 × 3
zero_matrix = []
for i in range(7):
    row = []
    for j in range(3):
        row.append(0)
    zero_matrix.append(row)

print("Zero Matrix (7x3):")
for row in zero_matrix:
    print(row)

3) Ones matrix of order 5 × 4
ones_matrix = []
for i in range(5):
    row = []
    for j in range(4):
        row.append(1)
    ones_matrix.append(row)

print("Ones Matrix (5x4):")
for row in ones_matrix:
    print(row)

Q3 A.2 Find the inverse of matrix A
A = [
    [1, 1, 1],
    [0, 1, 1],
    [0, 1, 1]
]
det = 0
for i in range(3):
    minor = 1
    for j in range(1, 3):
        for k in range(1, 3):
            if j != i and k != i:
                minor *= A[j][k]
    if i % 2 == 0: 
        det += A[0][i] * minor
    else:
        det -= A[0][i] * minor
print(f"Determinant of A: {det}")
if det != 0:
    print("The inverse exists (would be calculated if determinant was non-zero).")
else:
    print("Inverse does not exist because the determinant is 0.")

Q3 B.1 Find determinant and transpose
# Matrix A
A = [
    [1, 0, 5],
    [2, 1, 6],
    [3, 4, 0]
]
#determinant
det = 0
for i in range(3):
    minor = 1
    for j in range(1, 3):
        for k in range(1, 3):
            if j != i and k != i:
                minor *= A[j][k]
    if i % 2 == 0:
        det += A[0][i] * minor
    else:
        det -= A[0][i] * minor
print(f"Determinant of A: {det}")

# Matrix B
B = [
    [2, 5],
    [-1, 4]
]
#determinant
det_B = 0
for i in range(2):
    for j in range(2):
        if i == j:
            det_B += B[i][j]
print(f"Determinant DetB")

# Transpose of Matrix A
transpose_A = []
for i in range(3): 
    row = []
    for j in range(3):  
        row.append(A[j][i])
    transpose_A.append(row)

print("Transpose of A:")
for row in transpose_A:
    print(row)

# Transpose of Matrix B
transpose_B = []
for i in range(2):  
    row = []
    for j in range(2):  
        row.append(B[j][i])
    transpose_B.append(row)

print("Transpose of B:")
for row in transpose_B:
    print(row)

Q3 B.2 Write a Python program for A and B
# Matrices A and B
A = [
    [1, 2],
    [3, 4]
]
B = [
    [-1, 4],
    [2, 1]
]
# Matrix multiplication A * B
product = []
for i in range(2):
    row = []
    for j in range(2): 
        sum_product = 0
        for k in range(2): 
            sum_product += A[i][k] * B[k][j]
        row.append(sum_product)
    product.append(row)
print("Product of A and B:")
for row in product:
    print(row)

# Matrix addition A + B
addition = []
for i in range(2):  
    row = []
    for j in range(2):  
        row.append(A[i][j] + B[i][j])
    addition.append(row)
print("Addition of A and B:")
for row in addition:
    print(row)





