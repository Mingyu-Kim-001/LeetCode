from collections import defaultdict
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0
        for r in range(m):
            for c in range(n):
                matrix[r][c] += (matrix[r][c-1] if c > 0 else 0)
        
        for c1 in range(n):
            for c2 in range(c1, n):
                # do search for matrix[:][c1:c2]
                seen = defaultdict(int)
                seen[0] = 1
                res = 0
                for r in range(m):
                    res += matrix[r][c2] - (matrix[r][c1-1] if c1 > 0 else 0) #matrix[r][c1] +...+ matrix[r][c2]
                    if res - target in seen:
                        ans += seen[res-target]
                    seen[res] += 1
        
        return ans
                
        
        
        