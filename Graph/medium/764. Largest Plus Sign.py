class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        
        left = [[-1] * n for _ in range(n)]
        right = [[-1] * n for _ in range(n)]
        up = [[-1] * n for _ in range(n)]
        down = [[-1] * n for _ in range(n)]
        mines = set([(i,j) for i,j in mines])
        
        def vertical_DFS(start_i, i, j):
            if i < n and (i,j) not in mines:
                up[i][j] = start_i
                down[i][j] = vertical_DFS(start_i, i+1, j)
                return down[i][j]
            else:
                return i - 1
            
        def horizontal_DFS(start_j, i, j):
            if j < n and (i,j) not in mines:
                left[i][j] = start_j
                right[i][j] = horizontal_DFS(start_j, i, j+1)
                return right[i][j]
            else:
                return j - 1
                
            
        for i in range(n):
            for j in range(n):
                if (i,j) not in mines:
                    if left[i][j] == -1:
                        horizontal_DFS(j, i, j)
                    if up[i][j] == -1:
                        vertical_DFS(i, i, j)
        
        ans = 0
        for i in range(n):
            for j in range(n):
                if (i,j) not in mines:
                    ans = max(ans, min(j - left[i][j], right[i][j] - j, i - up[i][j], down[i][j] - i)+1)
        
        return ans