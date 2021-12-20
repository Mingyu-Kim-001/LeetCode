class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_x, min_y = m, n
        for x,y in ops:
            min_x = min(x, min_x)
            min_y = min(y, min_y)

        return min_x * min_y