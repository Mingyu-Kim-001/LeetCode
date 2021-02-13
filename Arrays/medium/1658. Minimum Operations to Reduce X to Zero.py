class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        prefixDic = {}
        prefix = 0
        total = sum(nums)
        prefixDic[0] = -1
        result = float("inf")
        for i,num in enumerate(nums):
            prefix+=num
            prefixDic[prefix] = i
            if prefix-(total-x) in prefixDic:
                result = min(result,len(nums) - (i-prefixDic[prefix-(total-x)]))
        return result if result!=float("inf") else -1