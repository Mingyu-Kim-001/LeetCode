class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        i = 0
        diff = float("inf")
        while i < len(nums):
            j, k = i + 1, len(nums) - 1
            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]
                
                if three_sum > target:
                    k -= 1
                elif three_sum < target:
                    j += 1
                else:
                    return target
                
                if abs(three_sum - target) < abs(diff):
                    diff = three_sum - target
            i += 1
        
        return target + diff
            
                    
                    