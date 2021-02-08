class Solution:
    def reachNumber(self, target: int) -> int:
        i = 0
        while i*(i+1)//2 < abs(target):
            i+=1
        while abs(i*(i+1)//2 - target)%2==1:
            i+=1
        return i