class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        maximum = [[0]*n for _ in range(m)]
        minimum = [[0]*n for _ in range(m)]
        maximum[0][0] = minimum[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0: 
                    continue
                candidate = []
                if i!=0: 
                    candidate.append(maximum[i-1][j]*grid[i][j])
                    candidate.append(minimum[i-1][j]*grid[i][j])
                if j!=0:
                    candidate.append(maximum[i][j-1]*grid[i][j])
                    candidate.append(minimum[i][j-1]*grid[i][j])
                maximum[i][j],minimum[i][j] = max(candidate),min(candidate)
        return -1 if maximum[m-1][n-1]<0 else maximum[m-1][n-1]%(pow(10,9)+7)