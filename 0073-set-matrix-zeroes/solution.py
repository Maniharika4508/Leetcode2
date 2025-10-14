class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
                m = len(matrix)
                n = len(matrix[0])
                zr = set()
                zc = set()

# First pass: record which rows and columns contain zeros
                for i in range(m):
                    for j in range(n):
                        if matrix[i][j] == 0:
                            zr.add(i)
                            zc.add(j)

                # Second pass: set recorded rows to zero
                for i in zr:
                    for j in range(n):
                        matrix[i][j] = 0

                # Third pass: set recorded columns to zero
                for j in zc:
                    for i in range(m):
                        matrix[i][j] = 0

