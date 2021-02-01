# Time: O(n)
# Space: O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        stack = 0
        for num in nums:
            if stack==0:
                majority = num
                stack+=1
            elif num==majority:
                stack+=1
            else:
                stack-=1
        return majority