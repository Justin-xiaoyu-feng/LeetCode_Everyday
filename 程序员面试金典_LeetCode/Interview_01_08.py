# 面试题 01.08. 零矩阵
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if matrix:
            row, column = [],[]
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] == 0:
                        row.append(i)
                        column.append(j)
            for ele in set(row):
                for i in range(len(matrix[0])):
                    matrix[ele][i] = 0
            for ele in set(column):
                for j in range(len(matrix)):
                    matrix[j][ele] = 0