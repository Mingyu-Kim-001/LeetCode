class union_find:
    def __init__(self,n):
        self.rank = [1]*n
        self.root = list(range(n))
        
    def find(self,p):
        if self.root[p] != p:
            self.root[p] = self.find(self.root[p])
        return self.root[p]
    
    def union(self,p,q):
        rootp,rootq = self.find(p),self.find(q)
        if self.rank[rootp] > self.rank[rootq]:
            self.root[rootq] = rootp
            self.rank[rootp] += self.rank[rootq]
        else:
            self.root[rootp] = rootq
            self.rank[rootq] += self.rank[rootp]
            
class Solution:
    def __init__(self):
        self.grid = None
        self.n = None
        self.is_visit = None 
        self.area = None
        self.uf = None
    
    def is_in_matrix(self,i,j):
        return 0 <= i < self.n and 0 <= j < self.n
    
    def DFS_max_area(self,i,j,root):
        result = 1
        self.is_visit[i][j] = True
        self.uf.union(root, i*self.n+j)
        for move_i, move_j in [[1,0],[0,1],[-1,0],[0,-1]]:
            new_i, new_j = i + move_i, j + move_j
            if self.is_in_matrix(new_i,new_j) and self.grid[new_i][new_j] and not self.is_visit[new_i][new_j]:
                result += self.DFS_max_area(new_i, new_j, root)
        return result
    
    def DFS_area_propagate(self, i, j, area):
        self.area[i][j] = area
        for move_i, move_j in [[1,0],[0,1],[-1,0],[0,-1]]:
            new_i, new_j = i + move_i, j + move_j
            if self.is_in_matrix(new_i,new_j) and self.grid[new_i][new_j] and self.area[new_i][new_j] == 0:
                self.DFS_area_propagate(new_i, new_j, area)
        
        
    def largestIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.n = len(grid)
        self.is_visit = [[False] * self.n for _ in range(self.n)]
        self.area = [[0] * self.n for _ in range(self.n)]
        self.uf = union_find(self.n*self.n)
        
        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i][j] and not self.is_visit[i][j]:
                    root = i * self.n + j
                    self.area[i][j] = self.DFS_max_area(i,j,root)
        
        for i in range(self.n):
            for j in range(self.n):
                if self.area[i][j] > 0:
                    self.DFS_area_propagate(i, j, self.area[i][j])
        
        ans = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i][j]:
                    ans = max(ans, self.area[i][j])
                    continue
                idx = []
                for new_i, new_j in [[i+1,j],[i,j+1],[i-1,j],[i,j-1]]:
                    if self.is_in_matrix(new_i,new_j):
                        for k,l in idx:
                            if self.uf.find(new_i*self.n+new_j) == self.uf.find(k*self.n+l):
                                break
                        else:
                            idx.append([new_i,new_j])
                ans = max(ans, 1+sum([self.area[k][l] for k,l in idx]))
        return ans
        



