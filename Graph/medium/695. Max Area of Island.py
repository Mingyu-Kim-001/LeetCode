class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        m = len(grid)
        n = len(grid[0])
        moves = [[1,0],[0,1],[-1,0],[0,-1]]
        def isInBoard(x,y):
            return 0<=x<m and 0<=y<n
        def DFS(x,y):
            grid[x][y] = 0
            area = 1
            for movex,movey in moves:
                newx,newy = x+movex,y+movey
                if isInBoard(newx,newy) and grid[newx][newy]==1:
                    area+= DFS(newx,newy)
            return area
        maxArea = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y]==1:
                    maxArea = max(maxArea,DFS(x,y))
        return maxArea