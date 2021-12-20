#Time: O(n)
from collections import deque
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        monoDec = deque([])
        result = float("-inf")
        for x,y in points:
            while monoDec and x-monoDec[0][1]>k:
                monoDec.popleft()
            if monoDec:
                result = max(result,monoDec[0][0]+x+y)
            while monoDec and monoDec[-1][0]<=y-x:
                monoDec.pop()
            monoDec.append([y-x,x])
        return result