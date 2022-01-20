class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def eating_time(piles, k):
            return sum([pile // k + (0 if pile % k == 0 else 1) for pile in piles])
        
        l, r = 1, max(piles)
        while l < r:
            m = (l + r) // 2
            if eating_time(piles, m) > h:
                l = m + 1
            else:
                r = m
        return l