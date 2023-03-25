# Формируется матрица F следующим образом: если в С сумма чисел, по периметру области 3 больше,
# чем произведение чисел по периметру области 2, то поменять в С симметрично области 2 и 3 местами,
# иначе В и Е поменять местами несимметрично.
# При этом матрица А не меняется. После чего вычисляется выражение: A*F+ K*F^T .
# Выводятся по мере формирования А, F и все матричные операции последовательно.

# B C    2
# E D  1   3
#        4


import random

def print_matrix(matrix):
    for row in matrix:
        for elem in row:
            print('{:4}'.format(elem), end=' ')
        print()
def paste_matrix(matrix_F, matrix, index, row_index):
    h = index
    for row in matrix:
        for element in row:
            matrix_F[row_index][index] = element
            index += 1
        row_index += 1
        index = h

try:

    K = int(input("Введите число K, являющееся коэффициентом при умножении: "))

    n = int(input("Введите число число N, больше или равное 5, являющееся порядком квадратной матрицы: "))

    while n < 5:
        n = int(input("Вы ввели число, неподходящее по условию, введите число N, больше или равное 5: "))
    del_n = n // 2
    fixik = del_n
    if n % 2 != 0:
        fixik += 1

    matrix_A = [[random.randint(-10, 10) for i in range(n)] for j in range(n)]
    print("\nМатрица A:")
    print_matrix(matrix_A)

    matrix_F = [[elem for elem in raw] for raw in matrix_A]
    print("\nМатрица F:")
    print_matrix(matrix_F)

    matrix_C = [[0 for i in range(del_n)] for j in range(del_n)]
    for i in range(del_n):
        for j in range(fixik, n):
            matrix_C[i][j - (fixik)] = matrix_A[i][j]
    print('\nПодматрица C:')
    print_matrix(matrix_C)

    matrix_B = [[0 for i in range(del_n)] for j in range(del_n)]
    for i in range(del_n):
        for j in range(del_n):
            matrix_B[i][j] = matrix_A[i][j]

    matrix_D = [[0 for i in range(del_n)] for j in range(del_n)]
    for i in range(del_n, n):
        for j in range(del_n):
            matrix_D[i - (fixik)][j] = matrix_A[i][j]

    matrix_E = [[0 for i in range(del_n)] for j in range(del_n)]
    for i in range(fixik, n):
        for j in range(fixik, n):
            matrix_E[i - (fixik)][j - (fixik)] = matrix_A[i][j]

    summa = 1
    for i in range(0, del_n):
        for j in range(0, del_n):
            if i == j and i <= (del_n - 1) // 2:
                summa *= matrix_C[i][j]
            elif i + j == del_n-1 and i <= (del_n - 1)//2:
                summa *= matrix_C[i][j]
    for j in range(1, del_n - 1):
        summa *= matrix_C[0][j]
    print("\nПроизведение чисел по периметру области 2:",summa)
    summa2 = 0
    for i in range(del_n - 1, -1, -1):
        for j in range(del_n - 1, -1, -1):
            if i + j == del_n-1 and i <= (del_n - 1)//2:
                summa2 += matrix_C[i][j]
            elif i == j and i > (del_n - 1) // 2:
                summa2 += matrix_C[i][j]
    for i in range(del_n - 2, 0, -1):
        summa2 += matrix_C[i][del_n - 1]
    print("Сумма чисел по периметру области 3:", summa2)

    matrix_F_dump = [[elem for elem in raw] for raw in matrix_F]
    if summa2 > summa:
        print("Сумма чисел больше в области 3 больше чем произведение чисел в области 2,", summa2 , ">", summa, ",меняем область 2 и 3 симметрично")
        g = del_n - 1
        for i in range(0, del_n):
            for j in range(0+i, del_n - i):
                matrix_C[i][j], matrix_C[g - j][g - i] = matrix_C[g - j][g - i], matrix_C[i][j]
        print('\nИзмененная подматрица С:')
        print_matrix(matrix_C)
    else:
        print("Сумма чисел больше в области 3 меньше чем произведение чисел в области 2,", summa2, "<", summa, ",меняем подматрицы B и E несимметрично")
        matrix_B, matrix_E = matrix_E, matrix_B

    matrix_F = matrix_A.copy()
    paste_matrix(matrix_F, matrix_B, 0, 0)
    paste_matrix(matrix_F, matrix_C, fixik, 0)
    paste_matrix(matrix_F, matrix_E, fixik, fixik)
    paste_matrix(matrix_F, matrix_D, 0, fixik)

    print('\nСозданная по условию матрица F:')
    print_matrix(matrix_F)

    matrix_F_transp = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            matrix_F_transp[i][j] = matrix_F[j][i]
    print("\nТранспонированая матрица F:")
    print_matrix(matrix_F_transp)

    matrix_AF = [[0 for i in range(n)] for j in range(n)]
    matrix_KF = matrix_F_transp.copy()
    for i in range(n):
        for j in range(n):
            for k in range(n):
                matrix_AF[i][j] += matrix_A[i][k] * matrix_F[k][j]
    print('\nРезультат A*F:')
    print_matrix(matrix_AF)

    for i in range(n):
        for j in range(n):
            matrix_KF[i][j] *= K
    print('\nРезультат K*F^T:')
    print_matrix(matrix_KF)

    matrix_res = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            matrix_res[i][j] = matrix_AF[i][j] - matrix_KF[i][j]
    print("\nРезультат A*F+K*F^T:")
    print_matrix(matrix_res)

except ValueError:
    print("Введенный символ не является числом. Перезапустите программу и введите число")
