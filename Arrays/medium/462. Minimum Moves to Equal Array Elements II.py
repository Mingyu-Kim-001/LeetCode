#Time: O(blogs)
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        
        if not nums: return 0
        n = len(nums)
        nums = sorted(nums)
        return sum([abs(i-nums[n//2]) for i in nums])