from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0]==1 or grid[n-1][n-1]==1: return -1
        visitWith = [[float("inf")]*n for _ in range(n)]
        bfs = deque([[0,0,1]])
        moves = [[1,1],[0,1],[1,0],[-1,0],[0,-1],[-1,1],[1,-1],[-1,-1]]
        def isInBoard(x,y):
            return 0<=x<n and 0<=y<n
        while bfs:
            x,y,count = bfs.popleft()
            if x==n-1 and y==n-1: return count
            if count>=visitWith[x][y]: continue
            visitWith[x][y] = count
            for movex,movey in moves:
                newx,newy = x+movex,y+movey
                if isInBoard(newx,newy) and grid[newx][newy]==0:
                    bfs.append([newx,newy,count+1])
        return -1