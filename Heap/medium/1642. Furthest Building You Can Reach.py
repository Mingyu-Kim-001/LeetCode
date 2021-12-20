import heapq as hq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        sum_heap = 0
        for i in range(1,len(heights)):
            if heights[i] - heights[i-1] > 0:
                to_overcome = heights[i] - heights[i-1]
                hq.heappush(heap,-to_overcome)
                sum_heap += to_overcome
                if sum_heap > bricks:
                    if ladders == 0:
                        return i - 1
                    sum_heap += hq.heappop(heap)
                    ladders -= 1
                # print(i,sum_heap,heap,ladders)
        return len(heights) - 1