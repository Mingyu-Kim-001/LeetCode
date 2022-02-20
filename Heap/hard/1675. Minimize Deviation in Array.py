import heapq as hq
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = [-num * 2 if num % 2 else -num for num in nums]
        hq.heapify(heap)
        minimum = -max(heap)
        ans = float("inf")
        while True:
            maximum = -hq.heappop(heap)
            ans = min(maximum - minimum, ans)
            if maximum % 2:
                break
            else:
                hq.heappush(heap, -maximum // 2)
                minimum = min(minimum, maximum // 2)
        return ans