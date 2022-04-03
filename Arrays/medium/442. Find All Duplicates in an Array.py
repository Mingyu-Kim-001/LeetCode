class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        while l <= r:
            num = nums[r]
            # if num is found twice
            if nums[abs(num)-1] < 0:
                nums[l], nums[r] = nums[r], nums[l]
                if (nums[l] < 0 and nums[r] > 0) or (nums[l] > 0 and nums[r] < 0):
                    nums[l], nums[r] = -nums[l], -nums[r]
                l += 1
            else:
                nums[abs(num)-1] *= -1
                r -= 1
        i = 0
        while i < len(nums):
            if i <= r:
                nums[i] = -nums[i] if nums[i] < 0 else nums[i]
                i += 1
            else:
                nums.pop()
        return nums