import heapq as hq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        hq.heapify(stones)
        while len(stones) > 1:
            stone1 = hq.heappop(stones)
            stone2 = hq.heappop(stones)
            if stone1 != stone2:
                hq.heappush(stones, -abs(stone1 - stone2))
        return -stones[0] if stones else 0
            