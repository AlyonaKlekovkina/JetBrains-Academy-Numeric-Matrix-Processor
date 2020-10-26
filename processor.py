from copy import deepcopy


def get_matrix(row, column):
    matrix = []
    for i in range(row):
        matrix.append([])
        x = input().split()
        for j in range(column):
            matrix[i].append((x[j]))
    return matrix


def multiply_matrix_by_const(matrix, x):
    global n_1, m_1
    matrix_multiplied_by_const = []
    for i in range(int(n_1)):
        matrix_multiplied_by_const.append([])
        for j in range(int(m_1)):
            matrix_multiplied_by_const[i].append(float(matrix[i][j]) * x)
    return matrix_multiplied_by_const


def multiply_matrices(a, b):
    global n_1, m_1
    matrices_multiplied = []
    for i in range(int(n_1)):
        matrices_multiplied.append([])
        for j in range(int(m_2)):
            multiplied = int()
            for k in range(int(m_1)):
                multiplied += float(a[i][k]) * float(b[k][j])
            matrices_multiplied[i].append(multiplied)
    return matrices_multiplied


def sum_matrices(a, b):
    global n_1, m_1
    summed_matrix = []
    for i in range(int(n_1)):
        summed_matrix.append([])
        for j in range(int(m_1)):
            summed_matrix[i].append(float(a[i][j]) + float(b[i][j]))
    return summed_matrix


def transposed_main_diagonal(matrix):
    d_transposed = []
    for i in range(int(n_1)):
        for j in range(int(m_1)):
            row = []
            for k in range(int(m_1)):
                row.append(matrix[k][i])
        d_transposed.append(row)
    return d_transposed


def transposed_side_diagonal(matrix):
    side_transposed = []
    for i in reversed(range(int(n_1))):
        for j in range(int(m_1)):
            row = []
            for k in reversed(range(int(m_1))):
                row.append(matrix[k][i])
        side_transposed.append(row)
    return side_transposed


def transposed_vertical_line(matrix):
    vertical_transposed = []
    for i in range(int(m_1)):
        for j in range(int(m_1)):
            row = []
            for k in reversed(range(int(m_1))):
                row.append(matrix[i][k])
        vertical_transposed.append(row)
    return vertical_transposed


def transposed_horizontal_line(matrix):
    horizontal_transposed = []
    for i in reversed(range(int(m_1))):
        for j in range(int(m_1)):
            row = []
            for k in range(int(m_1)):
                row.append(matrix[i][k])
        horizontal_transposed.append(row)
    return horizontal_transposed


def get_two_matrices():
    global n_1, m_1, n_2, m_2
    row_and_column_1 = input("Enter size of first matrix: ")
    n_1, m_1 = row_and_column_1.split()
    print("Enter first matrix:")
    matrix_a = get_matrix(int(n_1), int(m_1))
    row_and_column_2 = input("Enter size of second matrix: ")
    print("Enter second matrix:")
    n_2, m_2 = row_and_column_2.split()
    matrix_b = get_matrix(int(n_2), int(m_2))
    return matrix_a, matrix_b


def get_one_matrix():
    global n_1, m_1
    row_and_column_1 = input("Enter size of matrix: ")
    n_1, m_1 = row_and_column_1.split()
    print("Enter matrix: ")
    single_matrix = get_matrix(int(n_1), int(m_1))
    return single_matrix


def del_column(matrix, c):
    res_mat = deepcopy(matrix)
    for i in range(len(res_mat)):
        del res_mat[i][c]
    return res_mat


def del_row(matrix, c):
    res_mat = deepcopy(matrix)
    for i in range(len(res_mat)):
        del res_mat[c]
        return res_mat


def matrix_determinant(matrix):
    if len(matrix) == 1:
        return float(matrix[0][0])
    elif len(matrix) == 2:
        return (float(matrix[0][0]) * float(matrix[1][1])) - (float(matrix[0][1]) * float(matrix[1][0]))
    else:
        determinant = 0
        new_matrix = matrix[1:]
        for i in range(len(matrix)):
            multiplier = float(matrix[0][i])
            minor = del_column(new_matrix, i)
            if i % 2 != 0:
                multiplier = -multiplier
            determinant += multiplier * matrix_determinant(minor)
        return determinant


def adjoint_matrix(matrix):
    adjoint = []
    for i in range(len(matrix)):
        adjoint.append([])
        new_matrix = del_row(matrix, i)
        for j in range(len(matrix)):
            minor = del_column(new_matrix, j)
            multipl = pow(-1, (i + j))
            adjoint[i].append(multipl * float(matrix_determinant(minor)))
    return adjoint


def matrix_inverse(matrix):
    determ = matrix_determinant(matrix)
    adj = adjoint_matrix(matrix)
    transposed_adj = transposed_main_diagonal(adj)
    m = 1 / determ
    resulted = multiply_matrix_by_const(transposed_adj, m)
    return resulted


def print_result(matrix):
    print("The result is: ")
    for k in matrix:
        print(' '.join(map(str, k)))


while True:
    print("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n4. Transpose matrix\n5. Calculate a determinant\n6. Inverse matrix\n0. Exit")
    choice = int(input("Your choice: "))
    if choice == 1:
        matrix_a, matrix_b = get_two_matrices()
        if len(matrix_a) != len(matrix_b):
            print("The operation cannot be performed.\n")
        else:
            the_summed_matrix = sum_matrices(matrix_a, matrix_b)
            print_result(the_summed_matrix)
    elif choice == 2:
        matrix_a = get_one_matrix()
        multiplier = float((input("Enter constant: ")))
        multiplied_by_const_matrix = multiply_matrix_by_const(matrix_a, multiplier)
        print_result(multiplied_by_const_matrix)
    elif choice == 3:
        matrix_a, matrix_b = get_two_matrices()
        multiplied_matrices = multiply_matrices(matrix_a, matrix_b)
        print_result(multiplied_matrices)
    elif choice == 4:
        print("1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line")
        t_choice = int(input("Your choice: "))
        matrix_to_transpose = get_one_matrix()
        if t_choice == 1:
            main_diagonal_transposed = transposed_main_diagonal(matrix_to_transpose)
            print_result(main_diagonal_transposed)
        elif t_choice == 2:
            side_diagonal_transposed = transposed_side_diagonal(matrix_to_transpose)
            print_result(side_diagonal_transposed)
        elif t_choice == 3:
            vertical_line_transposed = transposed_vertical_line(matrix_to_transpose)
            print_result(vertical_line_transposed)
        elif t_choice == 4:
            horizontal_line_transposed = transposed_horizontal_line(matrix_to_transpose)
            print_result(horizontal_line_transposed)
    elif choice == 5:
        det_matrix = get_one_matrix()
        print("The result is:")
        print(matrix_determinant(det_matrix))
    elif choice == 6:
        matrix_to_calc = get_one_matrix()
        determinant = matrix_determinant(matrix_to_calc)
        if determinant == 0:
            print("This matrix doesn't have an inverse.")
        else:
            print_result((matrix_inverse(matrix_to_calc)))
    elif choice == 0:
        break
