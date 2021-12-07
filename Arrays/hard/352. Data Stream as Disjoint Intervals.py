import heapq as hq
class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, val: int) -> None:
        hq.heappush(self.intervals,[val, val])

    def getIntervals(self) -> List[List[int]]:
        temp_intervals = []
        while self.intervals:
            interval = hq.heappop(self.intervals)
            if not temp_intervals or temp_intervals[-1][-1] + 1< interval[0]:
                temp_intervals.append(interval)
            else:
                temp_intervals[-1][-1] = max(temp_intervals[-1][-1], interval[1])
        self.intervals = temp_intervals
        return self.intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()