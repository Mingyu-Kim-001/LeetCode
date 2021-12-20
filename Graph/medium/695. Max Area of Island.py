class Solution:
    def __init__(self):
        self.m = None
        self.n = None
        self.visit = None
        self.moves = [[1,0],[-1,0],[0,1],[0,-1]]
        self.grid = None
        self.this_area = 0
        self.ans = 0
        
    def is_in_board(self,i,j):
        return 0 <= i < self.m and 0 <= j < self.n
    
    def DFS(self,i,j):
        if self.visit[i][j]:
            return
        self.visit[i][j] = True
        self.this_area += 1
        self.ans = max(self.ans, self.this_area)
        for movei, movej in self.moves:
            newi, newj = i + movei, j + movej
            if self.is_in_board(newi,newj) and self.grid[newi][newj]:
                self.DFS(newi,newj)
        
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.m, self.n = len(grid), len(grid[0])
        self.visit = [[False]*self.n for _ in range(self.m)]
        self.grid = grid
        ans = 0
        
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] and not self.visit[i][j]:
                    self.this_area = 0
                    self.DFS(i,j)
    
        return self.ans