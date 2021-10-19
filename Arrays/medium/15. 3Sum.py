class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i1 = 0
        ans = []
        if len(nums) < 3:
            return []
        while i1 < len(nums) - 2:
            i2, i3 = i1 + 1, len(nums) - 1
            while i1 < i2 < i3:
                three_sum = nums[i1] + nums[i2] + nums[i3]
                if three_sum > 0:
                    i3 -= 1
                elif three_sum < 0:
                    i2 += 1
                else:
                    ans.append([nums[i1],nums[i2],nums[i3]])
                    while i2 < i3 and nums[i2] == nums[i2+1]:
                        i2 += 1
                    while i2 < i3 and nums[i3] == nums[i3-1]:
                        i3 -= 1
                    i2, i3 = i2 + 1, i3 - 1
            while i1 < len(nums) - 2 and nums[i1] == nums[i1+1]:
                i1 += 1
            i1 += 1
        return ans