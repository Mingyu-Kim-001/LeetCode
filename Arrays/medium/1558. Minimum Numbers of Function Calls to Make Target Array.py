class Solution:
    def minOperations(self, nums: List[int]) -> int:
        result = 0
        total = sum(nums)
        while total:
            for i in range(len(nums)):
                if nums[i]%2==1:
                    nums[i]-=1
                    result+=1
                    total-=1
            if total:
                nums = [i//2 for i in nums]
                total//=2
                result+=1
        return result