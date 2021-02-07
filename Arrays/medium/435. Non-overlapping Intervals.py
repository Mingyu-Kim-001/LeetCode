class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        end = float("-inf")
        result = 0
        for x,y in intervals:
            if x>=end:
                end = y
            else:
                result+=1
        return result