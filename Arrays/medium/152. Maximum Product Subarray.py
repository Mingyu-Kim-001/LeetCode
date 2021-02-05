class Solution:
    def findMin(self, nums) -> int:
        l = 0
        r = len(nums)-1
        if nums[r]>nums[l]: return nums[l]
        while l<r:
            mid = (l+r)//2
            if nums[mid]>=nums[l]:
                if nums[mid+1]<nums[l]:
                    return nums[mid+1]
                l = mid+1
            else:
                if nums[mid-1]>=nums[l]:
                    return nums[mid]
                r = mid-1
        return nums[r]