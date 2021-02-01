#Time: O(n)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = float("-inf")
        cons = 0
        for num in nums:
            if num==0:
                cons = 0
            else:
                cons+=1
            result = max(result,cons)
            
        return result