class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        m,n = len(matrix), len(matrix[0])
        prefix = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                prefix[i][j] = matrix[i][j]
                if i > 0:
                    prefix[i][j] += prefix[i-1][j]
                if j > 0:
                    prefix[i][j] += prefix[i][j-1]
                if i > 0 and j > 0:
                    prefix[i][j] -= prefix[i-1][j-1]
        self.prefix = prefix
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        ans = self.prefix[row2][col2]
        if row1 > 0:
            ans -= self.prefix[row1-1][col2]
        if col1 > 0:
            ans -= self.prefix[row2][col1-1]
        if row1 > 0 and col1 > 0:
            ans += self.prefix[row1-1][col1-1]
        return ans