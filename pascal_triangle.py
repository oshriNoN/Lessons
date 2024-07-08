
def pascal_value(i, j):
    if j == 0 or j == i:
        return 1
    return pascal_value(i - 1, j - 1) + pascal_value(i - 1, j)

def generate_pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(pascal_value(i, j))
        triangle.append(row)
    return triangle

n = 15
pascals_triangle = generate_pascal_triangle(n)
for row in pascals_triangle:
    print(row)