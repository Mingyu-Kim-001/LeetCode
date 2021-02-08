class Solution:
    def getMaxLen(self, nums) -> int:
        def getMaxWithoutZeros(nums):
            if len(nums)==0: return 0
            firstNegativeIndex = -1
            lastNegativeIndex = -1
            negativeCount = 0
            for i,num in enumerate(nums):
                if num<0:
                    if firstNegativeIndex<0: firstNegativeIndex = i
                    lastNegativeIndex = i
                    negativeCount+=1
            if negativeCount%2==0:
                return len(nums)
            return max(len(nums)-firstNegativeIndex-1,lastNegativeIndex)
        maxLen = -1
        preZero = -1
        for i,num in enumerate(nums):
            if num==0:
                maxLenCand = getMaxWithoutZeros(nums[preZero+1:i])
                if maxLen<maxLenCand:
                    maxLen = maxLenCand
                preZero = i
#         if maxLen==-1:
#             return getMaxWithoutZeros(nums)
        return max(maxLen,getMaxWithoutZeros(nums[preZero+1:]))