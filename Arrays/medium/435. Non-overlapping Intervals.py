class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        end = float("-inf")
        result = 0
        intervals.sort(key=lambda x:x[1])
        for interval in intervals:
            if interval[0] < end:
                result += 1
            else:
                end = interval[1]
        return result