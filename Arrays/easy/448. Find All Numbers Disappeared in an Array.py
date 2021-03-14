#Time: O(n), Space : O(1)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        i = 0
        while i < len(nums):
            num = nums[i]
            nums[(num-1)%(2*n)] += 2 * n
            i += 1
        for i,num in enumerate(nums):
            if num <= n:
                result.append(i+1)
        return result