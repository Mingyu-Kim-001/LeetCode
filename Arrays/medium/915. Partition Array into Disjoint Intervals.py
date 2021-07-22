class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        left_max = -1
        cur_max = -1
        for i,num in enumerate(nums):
            cur_max = max(cur_max, num)
            if left_max < 0 or left_max > num:
                bound = i
                left_max = cur_max
        return bound + 1