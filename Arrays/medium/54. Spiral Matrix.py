class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        direction = 0 # 0 for right, 1 for down, 2 for left, 3 for up
        move = {0 : [0,1], 1 : [1,0], 2 : [0,-1], 3 : [-1,0]}
        x = y = 0
        visit = [[False] * n for _ in range(m)]
        visit[0][0] = True
        ans = [matrix[0][0]]
        while len(ans) < m * n:
            rotate = 0
            while rotate < 4:
                move_x, move_y = move[direction]
                new_x, new_y = x + move_x, y + move_y
                if 0 <= new_x < m and 0 <= new_y < n and not visit[new_x][new_y]:
                    x, y = new_x, new_y
                    break
                direction = (direction+1) % 4
                rotate += 1
            ans.append(matrix[x][y])
            visit[x][y] = True
        return ans