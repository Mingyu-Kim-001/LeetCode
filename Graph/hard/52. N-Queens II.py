class Solution:
    def __init__(self):
        self.coordinates = []
        self.col_attacked = set()
        self.diff_attacked = set()
        self.sum_attacked = set()
        self.n = None
        self.ans = 0
    def is_attacked(self,row,col):
        return col in self.col_attacked or row - col in self.diff_attacked or row + col in self.sum_attacked
    
    def set_queen(self,row,col):
        self.coordinates.append([row,col])
        self.col_attacked.add(col)
        self.diff_attacked.add(row-col)
        self.sum_attacked.add(row+col)
    
    def remove_queen(self,row,col):
        self.coordinates.pop()
        self.col_attacked.remove(col)
        self.diff_attacked.remove(row-col)
        self.sum_attacked.remove(row+col) 
        
    def DFS(self,row):
        for col in range(self.n):
            if not self.is_attacked(row,col):
                self.set_queen(row,col)
                if row == self.n - 1:
                    self.ans += 1
                else:
                    self.DFS(row+1)
                self.remove_queen(row,col)
        
    def totalNQueens(self, n: int) -> int:
        self.n = n
        self.DFS(0)
        return self.ans