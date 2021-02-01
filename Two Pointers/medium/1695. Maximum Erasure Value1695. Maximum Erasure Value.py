# Time: O(n)
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0
        r = 1
        unique_window = set()
        unique_window_sum = 0
        result = 0
        while r<=len(nums):
            if nums[r-1] in unique_window:
                while l<r and nums[l]!=nums[r-1]:
                    unique_window.remove(nums[l])
                    unique_window_sum-=nums[l]
                    l+=1
                l+=1
            else:
                unique_window.add(nums[r-1])
                unique_window_sum+=nums[r-1]
                result = max(result,unique_window_sum)
            r+=1
        return result