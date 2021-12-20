class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def is_in_board(x,y):
            return 0 <= x < m and 0 <= y < n
        
        minute = 0
        while True:
            rottened = []
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 2:
                        for adj_i, adj_j in [[1,0],[0,1],[-1,0],[0,-1]]:
                            new_i, new_j = i + adj_i, j + adj_j
                            if is_in_board(new_i, new_j) and grid[new_i][new_j] == 1:
                                rottened.append([new_i,new_j])
            if not rottened:
                break
            for i, j in rottened:
                grid[i][j] = 2
            minute += 1
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return minute