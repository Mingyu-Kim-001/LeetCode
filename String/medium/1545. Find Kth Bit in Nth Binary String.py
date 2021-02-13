#Time: O(n)
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        i = 1
        k = k-1
        invert = False
        while (1<<i) - 1<k:
            i+=1
        while k>0:
            if k== (1<<(i-1))-1: return "1" if not invert else "0"
            elif k>(1<<(i-1))-1:
                k = (1<<i)-2 - k
                invert = not invert
            i-=1
        return "0" if not invert else "1"