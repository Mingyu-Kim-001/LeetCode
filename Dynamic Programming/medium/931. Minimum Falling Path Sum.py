class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(n):
                if i==n-1:
                    dp[i][j] = matrix[i][j]
                else:
                    dp[i][j] = min([dp[i+1][max(j-1,0)],dp[i+1][j],dp[i+1][min(j+1,n-1)]]) + matrix[i][j]
        return min(dp[0])