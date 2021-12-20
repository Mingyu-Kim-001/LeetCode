#Time: O(mn). Typical DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        moves = [[1,0],[0,1],[-1,0],[0,-1]]
        def isInBoard(x,y):
            return 0<=x<m and 0<=y<n
        def DFS(x,y):
            grid[x][y] = "-1"
            for movex,movey in moves:
                newx,newy = x+movex,y+movey
                if isInBoard(newx,newy) and grid[newx][newy]=="1":
                    DFS(newx,newy)
        result = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y]=="1":
                    DFS(x,y)
                    result+=1
        return result