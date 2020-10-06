def get_matrix(row, column):
    matrix = []
    for i in range(row):
        matrix.append([])
        x = input().split()
        for j in range(column):
            matrix[i].append(int(x[j]))
    return matrix


def multiply_matrix(x):
    multiplied_matrix = []
    for i in range(int(n_1)):
        multiplied_matrix.append([])
        for j in range(int(m_1)):
            multiplied_matrix[i].append(matrix_a[i][j] * x)
    return multiplied_matrix


row_and_column_1 = input()
n_1, m_1 = row_and_column_1.split()
matrix_a = get_matrix(int(n_1), int(m_1))
multiplier = int(input())
result = multiply_matrix(multiplier)

for k in result:
    print(' '.join(map(str, k)))


