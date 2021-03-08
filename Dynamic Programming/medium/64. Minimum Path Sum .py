from collections import deque
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        dp = [[0]*n for _ in range(m)]
        
        dp[0][0] = grid[0][0]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j > 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                if j == 0 and i > 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                if i > 0 and j > 0:
                    dp[i][j] = min(dp[i][j-1],dp[i-1][j]) + grid[i][j]
        
        return dp[-1][-1]