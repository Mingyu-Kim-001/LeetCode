#Time: O(mn)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if not m or not n: return 0
        def isInBoard(x,y):
            return 0<=x<m and 0<=y<n
        moves = [[0,1],[1,0],[-1,0],[0,-1]]
        visit = [[False]*n for _ in range(m)]
        
        
        def DFS(x,y):
            area = 1
            visit[x][y] = True
            for movex, movey in moves:
                newx,newy = x + movex,y+movey
                if isInBoard(newx,newy) and not visit[newx][newy] and grid[newx][newy]==1:
                    area+=DFS(newx,newy)
            return area
        
        result = 0
        for x in range(m):
            for y in range(n):
                if not visit[x][y] and grid[x][y]==1:
                    result = max(result,DFS(x,y))
        return result