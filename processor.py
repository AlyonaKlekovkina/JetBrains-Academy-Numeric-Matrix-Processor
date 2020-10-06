def get_matrix(row, column):
    matrix = []
    for i in range(row):
        matrix.append([])
        x = input().split()
        for j in range(column):
            matrix[i].append(int(x[j]))
    return matrix


def sum_matrices(a, b):
    summed_matrix = []
    for i in range(int(n_1)):
        summed_matrix.append([])
        for j in range(int(m_1)):
            summed_matrix[i].append(a[i][j] + b[i][j])
    return summed_matrix


row_and_column_1 = input()
n_1, m_1 = row_and_column_1.split()
matrix_a = get_matrix(int(n_1), int(m_1))
row_and_column_2 = input()
n_2, m_2 = row_and_column_2.split()
matrix_b = get_matrix(int(n_2), int(m_2))

if row_and_column_1 != row_and_column_2:
    print("ERROR")
else:
    matrix_c = sum_matrices(matrix_a, matrix_b)
    for k in matrix_c:
        print(' '.join(map(str, k)))


