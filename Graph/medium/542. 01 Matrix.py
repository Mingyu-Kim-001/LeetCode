from collections import deque
class Solution:
    def is_in_matrix(self, i, j, m, n):
        return 0 <= i < m and 0 <= j < n
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        min_distance = [[float("inf")] * n for _ in range(m)]
        bfs = deque([])
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    min_distance[i][j] = 0
                    bfs.append([i,j,0])
                    
        while bfs:
            i, j, dist = bfs.popleft()
            for i_move, j_move in [[1,0],[0,1],[0,-1],[-1,0]]:
                new_i, new_j = i + i_move, j + j_move
                if self.is_in_matrix(new_i, new_j, m, n) and min_distance[new_i][new_j] == float("inf"):
                    min_distance[new_i][new_j] = dist + 1
                    bfs.append([new_i, new_j, dist+1])
        
        return min_distance
                    