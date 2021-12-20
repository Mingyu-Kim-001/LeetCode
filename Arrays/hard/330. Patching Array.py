class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        end = n_patches = i = 0
        
        while end < n:
            if i < len(nums) and end >= nums[i] - 1:
                end += nums[i]
                i += 1
            else:
                end = 2 * end + 1 #patch = end + 1
                n_patches += 1

        return n_patches