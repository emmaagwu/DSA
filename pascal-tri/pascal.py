#!/usr/bin/env python3
from typing import List

def pascal(n: int) -> List[List[int]]:
    """ this function takes an integer n and
        returns pascal triangle with n number of rows
    """
    matrix = []
    if not isinstance(n, int) or n <= 0:
        return matrix
    matrix = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(matrix[i - 1]) - 1):
            temp.append(matrix[i - 1][j] + matrix[i - 1][j + 1])
        temp.append(1)
        matrix.append(temp)
    return matrix

if __name__ == '__main__':
    print(pascal(6))
