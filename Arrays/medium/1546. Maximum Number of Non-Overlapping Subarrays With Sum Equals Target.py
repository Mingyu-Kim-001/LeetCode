#Time: O(n)
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        prefixSet = set([0])
        prefix = result = 0
        for num in nums:
            prefix+=num
            if prefix-target in prefixSet:
                result+=1
                prefix = 0
                prefixSet = set([0])
            prefixSet.add(prefix)
        return result