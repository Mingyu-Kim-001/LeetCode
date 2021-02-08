class Solution:
    def minOperations(self, nums) -> int:
        result = 0
        while sum(nums)>0:
            for i in range(len(nums)):
                if nums[i]%2==1:
                    nums[i]-=1
                    result+=1
            if sum(nums)>0:
                for i in range(len(nums)):
                    if nums[i]!=0:
                        nums[i]/=2
                result+=1
        return result