from collections import Counter
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        powerOfTwo = 1
        while len(str(powerOfTwo))<=len(str(N)):
            if len(str(powerOfTwo))<=len(str(N)) and Counter(str(powerOfTwo))==Counter(str(N)): return True
            powerOfTwo*=2
        return False