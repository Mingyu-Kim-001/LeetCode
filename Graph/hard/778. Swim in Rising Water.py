from collections import deque
class Solution:
    def __init__(self):
        self.grid = None
        self.n = None
    def isInBoard(self,x,y):
        return 0 <= x < self.n and 0 <= y < self.n
        
    def isPossible(self, t):
        visit = [[False]*self.n for _ in range(self.n)]
        moves = [[1,0],[0,1],[-1,0],[0,-1]]
        bfs = deque([[0,0]])
        while bfs:
            x, y = bfs.popleft()
            if visit[x][y]:
                continue
            visit[x][y] = True
            for movex, movey in moves:
                newx, newy = x + movex, y + movey
                if self.isInBoard(newx,newy) and not visit[newx][newy] and (self.grid[newx][newy] <= t):
                    if (newx,newy) == (self.n - 1, self.n - 1):
                        return True
                    bfs.append([newx,newy])
        return False
        
    def swimInWater(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.n = len(grid)
        if self.isPossible(grid[0][0]):
            return grid[0][0]
        l = grid[0][0]
        r = self.n * self.n - 1
        while l < r:
            if r == l + 1:
                return r
            m = (l + r) // 2
            if self.isPossible(m):
                r = m
            else:
                l = m