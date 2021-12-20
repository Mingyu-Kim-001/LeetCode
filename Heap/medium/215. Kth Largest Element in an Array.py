#Time: O(nlogk)
import heapq as hq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap)<k:
                hq.heappush(heap,num)
            else:
                candidate = hq.heappop(heap)
                hq.heappush(heap,max(candidate,num))
        return hq.heappop(heap)