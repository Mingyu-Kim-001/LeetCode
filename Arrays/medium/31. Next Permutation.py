#Time: O(n)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:return nums
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                break
        else:
            nums.reverse()
            return
        for j in range(len(nums)-1,-1,-1):
            if nums[i]<nums[j]:
                nums[i],nums[j] = nums[j],nums[i]
                break
        temp = nums[i+1:]
        temp.reverse()
        for k in range(i+1,len(nums)):
            nums[k] = temp[k-i-1]
        return
