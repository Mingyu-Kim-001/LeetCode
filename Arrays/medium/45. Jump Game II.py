class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        ans = i = 0
        cur_max = next_max = nums[0]
        
        while i < len(nums):
            while i <= cur_max and i < len(nums):
                next_max = max(next_max,i+nums[i])
                i += 1
            cur_max = next_max
            ans += 1
            
        return ans