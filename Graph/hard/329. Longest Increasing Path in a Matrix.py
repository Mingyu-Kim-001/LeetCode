class Solution:
    def longestIncreasingPath(self, matrix) -> int:
        m,n = len(matrix), len(matrix[0])
        moves = [[1,0],[0,1],[-1,0],[0,-1]]
        longest_len = [[1]*n for _ in range(m)]
        is_visit = [[False]*n for _ in range(m)]
        def is_in_board(x,y):
            return 0 <= x < m and 0 <= y < n
        def DFS(x,y):
            if is_visit[x][y]:
                return longest_len[x][y]
            is_visit[x][y] = True
            for movex,movey in moves:
                newx,newy = x + movex, y + movey
                if is_in_board(newx,newy) and matrix[newx][newy] < matrix[x][y]:
                    longest_len[x][y] = max(longest_len[x][y], DFS(newx,newy)+1)
            return longest_len[x][y]
        ans = -1
        for i in range(m):
            for j in range(n):
                ans = max(ans,DFS(i,j))
        return ans