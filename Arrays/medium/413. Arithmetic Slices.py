#Time: O(n)
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        arithmetic_stack = result = 0
        for i in range(len(A)):
            if i<len(A)-2 and A[i+1]-A[i]==A[i+2]-A[i+1]:
                arithmetic_stack = 3 if arithmetic_stack ==0 else arithmetic_stack+1
            elif arithmetic_stack!=0:
                result+=(arithmetic_stack-2)*(arithmetic_stack-1)//2
                arithmetic_stack = 0
        return resultx