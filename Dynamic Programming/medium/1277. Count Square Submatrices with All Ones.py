#Time: O(MN)
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ones = sum([sum(row) for row in matrix])
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or not matrix[i][j]:
                    continue
                matrix[i][j] = min([matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1]]) + 1
        return sum([sum(row) for row in matrix])