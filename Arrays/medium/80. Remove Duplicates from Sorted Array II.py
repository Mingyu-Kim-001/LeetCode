class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = fast = 0
        while fast < len(nums):
            while fast < len(nums) - 2 and nums[fast] == nums[fast + 2]:
                fast += 1
            nums[slow] = nums[fast]
            fast += 1
            slow += 1
        while slow < len(nums):
            nums.pop()
        return
            