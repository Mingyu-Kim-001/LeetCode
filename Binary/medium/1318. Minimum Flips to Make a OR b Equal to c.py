#Time: O(logn)
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        result = 0
        while a or b or c:
            if c%2==1:
                result+=(1 if a%2==0 and b%2==0 else 0)
            else:
                result+=(1 if a%2==1 else 0) + (1 if b%2==1 else 0)
            c//=2
            a//=2
            b//=2
        return result