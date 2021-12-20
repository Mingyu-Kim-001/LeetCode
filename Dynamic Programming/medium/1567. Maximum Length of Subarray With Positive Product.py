#Time: O(n)
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        posLen = negLen = result = 0
        for num in nums:
            if num>0:
                if negLen>0: 
                    negLen+=1
                posLen+=1
            elif num<0:
                posLen,negLen = (negLen+1 if negLen>0 else 0), (posLen+1)
            else:
                posLen = negLen = 0
            result = max(result,posLen)
        return result