#Time: O(n)
from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)
        result = 0
        for i in counter:
            if i+1 in counter:
                result = max(result,counter[i]+counter[i+1])
        return result