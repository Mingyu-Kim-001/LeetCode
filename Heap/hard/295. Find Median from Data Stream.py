import heapq as hq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left = [] #maxheap
        self.right = [] #minheap
        self.n = 0

    def addNum(self, num: int) -> None:
        if self.n % 2 == 1:
            if self.right[0] >= num:
                hq.heappush(self.left, -num)
            else:
                hq.heappush(self.left, -hq.heappop(self.right))
                hq.heappush(self.right, num)
        else:
            if not self.left or -self.left[0] <= num:
                hq.heappush(self.right, num)
            else:
                hq.heappush(self.right, -hq.heappop(self.left))
                hq.heappush(self.left, -num)
        self.n += 1

    def findMedian(self) -> float:
        if self.n % 2 == 0:
            return (self.right[0] - self.left[0]) / 2
        else:
            return self.right[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()