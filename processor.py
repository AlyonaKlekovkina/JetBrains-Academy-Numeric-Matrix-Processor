def get_matrix(row, column):
    matrix = []
    for i in range(row):
        matrix.append([])
        x = input().split()
        for j in range(column):
            matrix[i].append((x[j]))
    return matrix


def multiply_matrix_by_const(x):
    global n_1, m_1, n_2, m_2
    matrix_multiplied_by_const = []
    for i in range(int(n_1)):
        matrix_multiplied_by_const.append([])
        for j in range(int(m_1)):
            matrix_multiplied_by_const[i].append(float(matrix_a[i][j]) * x)
    return matrix_multiplied_by_const


def multiply_matrices(a, b):
    global n_1, m_1, n_2, m_2
    multiplication = []
    for i in range(int(n_1)):
        multiplication.append([])
        for j in range(int(m_2)):
            multiplied = int()
            for k in range(int(m_1)):
                multiplied += float(a[i][k]) * float(b[k][j])
            multiplication[i].append(multiplied)
    return multiplication


def sum_matrices(a, b):
    global n_1, m_1, n_2, m_2
    summed_matrix = []
    for i in range(int(n_1)):
        summed_matrix.append([])
        for j in range(int(m_1)):
            summed_matrix[i].append(float(a[i][j]) + float(b[i][j]))
    return summed_matrix


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


while True:
    print("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n0. Exit")
    choice = int(input("Your choice: "))
    if choice == 1:
        matrix_a, matrix_b = get_two_matrices()
        if len(matrix_a) != len(matrix_b):
            print("The operation cannot be performed.\n")
        else:
            print("The result is: ")
            matrix_c = sum_matrices(matrix_a, matrix_b)
            for k in matrix_c:
                print(' '.join(map(str, k)))

    elif choice == 2:
        row_and_column_1 = input("Enter size of matrix: ")
        n_1, m_1 = row_and_column_1.split()
        print("Enter matrix: ")
        matrix_a = get_matrix(int(n_1), int(m_1))
        multiplier = float((input("Enter constant: ")))
        result = multiply_matrix_by_const(multiplier)
        print("The result is: ")
        for k in result:
            print(' '.join(map(str, k)))

    elif choice == 3:
        matrix_a, matrix_b = get_two_matrices()
        result_matrix = multiply_matrices(matrix_a, matrix_b)
        for k in result_matrix:
            print(' '.join(map(str, k)))
    elif choice == 0:
        break
