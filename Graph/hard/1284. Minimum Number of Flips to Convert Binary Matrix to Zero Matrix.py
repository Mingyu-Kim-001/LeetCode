from collections import deque, defaultdict
class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        cur = sum([mat[i][j] << (i * n + j) for i in range(m) for j in range(n)])
        flips = defaultdict(int)
        for i in range(m):
            for j in range(n):
                for x,y in [(i+1,j),(i,j+1),(i-1,j),(i,j-1),(i,j)]:
                    if 0 <= x < m and 0 <= y < n:
                        flips[i * n + j] += (1 << (x * n + y))
                    
        bfs = deque([[cur,0]])
        seen = set([cur])
        while bfs:
            cur, flip_count = bfs.popleft()
            if cur == 0:
                return flip_count
            for i in range(m):
                for j in range(n):
                    new_cur = new_cur = cur ^ flips[i * n + j]
                    if not new_cur in seen:
                        bfs.append([new_cur, flip_count + 1])
                        seen.add(new_cur)
        return -1
        
                
                