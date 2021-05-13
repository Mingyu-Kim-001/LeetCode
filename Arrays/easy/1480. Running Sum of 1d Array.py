class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        for i,num in enumerate(nums):
            if not ans:
                ans.append(num)
            else:
                ans.append(ans[-1]+num)
        return ans