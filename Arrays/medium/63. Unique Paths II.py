class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1]:
            return 0
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        way_count = [[0]*n for _ in range(m)]
        way_count[0][0] = 1
        for i in range(m):
            for j in range(n):
                way_count[i][j] += (way_count[i-1][j] if i > 0 and not obstacleGrid[i-1][j] else 0) + (way_count[i][j-1] if j > 0 and not obstacleGrid[i][j-1] else 0)
        
        return way_count[-1][-1]