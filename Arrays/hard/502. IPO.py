import heapq as hq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(capital)
        n_pjs = idx = 0
        profit_heap = []
        capitals_and_profits = sorted([(c,p) for c, p in zip(capital, profits)])
        while n_pjs < k:
            while idx < n and capitals_and_profits[idx][0] <= w:
                hq.heappush(profit_heap, -capitals_and_profits[idx][1])
                idx += 1
            if not profit_heap:
                return w
            w += -hq.heappop(profit_heap)
            n_pjs += 1
        return w