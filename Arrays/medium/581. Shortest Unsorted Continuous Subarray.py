#Time: O(n)
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        minStack = []
        maxStack = []
        for i,num in enumerate(nums):
            while minStack and minStack[-1][0]>num:
                minStack.pop()
            minStack.append([num,i])
        for i,num in enumerate(nums[::-1]):
            while maxStack and maxStack[-1][0]<num:
                maxStack.pop()
            maxStack.append([num,i])
        for j,(num,i) in enumerate(minStack):
            if j!=i: 
                start = j
                break
        else:
            return 0
        for j,(num,i) in enumerate(maxStack):
            if j!=i: 
                end = j
                break
        return (len(nums)-1-end)-start + 1