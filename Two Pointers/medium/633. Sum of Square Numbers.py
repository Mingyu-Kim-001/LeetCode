#Time: O(n)
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        while i*i<c: i+=1
        l,r = 0,i
        while l<=r:
            squareSum = l*l + r*r
            if squareSum<c:
                l+=1
            elif squareSum>c:
                r-=1
            else:
                return True
        return False