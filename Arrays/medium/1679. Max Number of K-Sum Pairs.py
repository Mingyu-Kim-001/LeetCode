#Time: O(n)
from collections import defaultdict
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        result = 0
        for num in nums:
            if counter[k-num]>0:
                counter[k-num]-=1
                result+=1
            else:
                counter[num]+=1
        return result