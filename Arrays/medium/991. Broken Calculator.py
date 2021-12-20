#Time: O(logY)
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        if X>Y: return X-Y
        y = Y
        opCount = 0
        while X<y:
            if y%2==1: y+=1
            else: y//=2
            opCount+=1
        return X-y + opCount