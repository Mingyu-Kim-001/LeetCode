class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        self.ans = 0
        maxlen = sum([grid[i][j] != -1 for i in range(m) for j in range(n)])
        
        start_i, start_j = [(i,j) for i in range(m) for j in range(n) if grid[i][j] == 1][0]
        def is_in_board(i,j):
            return 0 <= i < m and 0 <= j < n
        
        def DFS(i, j, len_route):
            if not is_in_board(i,j) or grid[i][j] < 0:
                return
            len_route += 1
            if grid[i][j] == 2 and len_route == maxlen:
                self.ans += 1
            elif grid[i][j] == 0 or grid[i][j] == 1:
                grid[i][j] = -2
                DFS(i+1, j, len_route)
                DFS(i-1, j, len_route)
                DFS(i, j+1, len_route)
                DFS(i, j-1, len_route)
                grid[i][j] = 0
            len_route -= 1
            return
            
        DFS(start_i, start_j, 0)
        return self.ans
                
            