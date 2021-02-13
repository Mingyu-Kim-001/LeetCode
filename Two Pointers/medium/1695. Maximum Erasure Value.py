class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        windowSet = set()
        #windowSet : set of nums[l],...,nums[r]
        windowSum = 0 # = sum(nums[l:r+1])
        l = r = 0
        result = float("-inf")
        while l<=r<len(nums):
            if not nums[r] in windowSet:
                windowSet.add(nums[r])
                windowSum+=nums[r]
                result = max(result,windowSum)
                r+=1
            else:
                windowSet.remove(nums[l])
                windowSum-=nums[l]
                l+=1
        return result