# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

#Time: O(logn)
class Solution:
    def guessNumber(self, n: int) -> int:
        l,r = 1,n
        while l<=r:
            m = (l+r)//2
            g = guess(m)
            if g==-1:
                r = m-1
            elif g==0:
                return m
            else:
                l = m+1