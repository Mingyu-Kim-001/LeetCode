class Solution:
    def is_not_decreasing(self,nums):
        for i in range(len(nums)):
            if i > 0 and nums[i-1] > nums[i]:
                return False
        return True
    def checkPossibility(self, nums: List[int]) -> bool:
        a,b = nums[:],nums[:]
        for i,num in enumerate(nums):
            if i > 0 and nums[i-1] > nums[i]:
                a[i] = nums[i-1]
                b[i-1] = nums[i]
                break
        return self.is_not_decreasing(a) or self.is_not_decreasing(b)