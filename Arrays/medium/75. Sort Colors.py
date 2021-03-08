#Time: O(n)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        zero_idx = 0
        while i < len(nums):
            if nums[i] == 0:
                nums[zero_idx],nums[i] = nums[i],nums[zero_idx]
                zero_idx += 1
            i += 1
        i = one_idx = zero_idx
        while i < len(nums):
            if nums[i] == 1:
                nums[one_idx],nums[i] = nums[i],nums[one_idx]
                one_idx += 1
            i += 1