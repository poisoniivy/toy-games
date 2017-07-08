"""
Write an algorithm such that if an element in an MxN matrix is 0,
its entire row and column is set to 0.

Input:
[[1, 0. 1]
 [0, 1, 1]
 [1, 1, 1]]

Output:
[[0, 0, 0]
 [0, 0, 0]
 [0. 0. 1]]

 - keep track of all rows that have 0s (iterate through) rows
 - keep track to see if cols have 0s
"""

def zero_matrix(matrix):

    row_zero = [1] * len(matrix)
    col_zero = [1] * len(matrix[0])

    for row in matrix:
        for i, col in enumerate(row):
            if col == 0:
                col_zero[i] = 0
        if 0 in row:
            row_zero.append(0)
        else:
            row_zero.append(1)

    new_matrix = []

    for i in len(row_zero)
        if 



