#Time:O(n)
from collections import defaultdict
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:return nums[0]
        if len(nums)==2: return max(nums)
        dp0 = defaultdict(int) #dp0[j] represents the maximum profit when house 0 is not robged, and house j is robbed 
        dp1 = defaultdict(int) #dp1[j] represents the maximum profit when house 0 is robged, and house j is robbed 
        for j in range(1,len(nums)):
            dp0[j] = max(dp0[j-2],dp0[j-3]) + nums[j]
        for j in range(len(nums)):
            dp1[j] = max(dp1[j-2],dp1[j-3]) + nums[j]
        return max(dp0[len(nums)-1],dp0[len(nums)-2],dp1[len(nums)-2],dp1[len(nums)-3])
        