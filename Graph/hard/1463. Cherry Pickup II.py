class Solution:
    def get_max_score(self, r1, r2, max_score_from_prev_row):
        cand = []
        for x in [r1 - 1, r1, r1 + 1]:
            for y in [r2 - 1, r2, r2 + 1]:
                if 0 <= x < self.n and 0 <= y < self.n:
                    cand.append(max_score_from_prev_row[x][y])
        return max(cand)
        
    def cherryPickup(self, grid: List[List[int]]) -> int:
        self.m, self.n = len(grid), len(grid[0])
        max_score = [[-1] * self.n for _ in range(self.n)]
        max_score[0][self.n-1] = grid[0][0] + grid[0][self.n-1]
        for row in range(1, self.m):
            
            max_score2 = [[-1] * self.n for _ in range(self.n)]
            for r1 in range(self.n):
                for r2 in range(self.n):
                    score = self.get_max_score(r1, r2, max_score)
                    if score >= 0:
                        max_score2[r1][r2] = score + (grid[row][r1] + grid[row][r2] if r1 != r2 else grid[row][r1])
            max_score = max_score2
        return max([max(row) for row in max_score])
        