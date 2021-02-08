class Solution:
    def movesToMakeZigzag(self, nums) -> int:
        bigEvenResult = 0
        for i in range(len(nums)):
            if i%2==1:
                if nums[i-1]<=nums[i]:
                    bigEvenResult+= nums[i] - nums[i-1] + 1
                    if i+1<len(nums) and nums[i-1]-1>=nums[i+1]:
                        bigEvenResult+= nums[i-1] - nums[i+1]
                elif i+1<len(nums) and nums[i]>=nums[i+1]:
                    bigEvenResult+= nums[i] - nums[i+1] + 1
        bigOddResult = 0
        
        for i in range(len(nums)):
            if i%2==0:
                if i-1>=0 and nums[i-1]<=nums[i]:
                    bigOddResult+= nums[i] - nums[i-1] + 1
                    if i+1<len(nums) and nums[i-1]-1>=nums[i+1]:
                        bigOddResult+= nums[i-1] - nums[i+1]
                elif i+1<len(nums) and nums[i]>=nums[i+1]:
                    bigOddResult+= nums[i] - nums[i+1] + 1
        return min(bigEvenResult,bigOddResult)