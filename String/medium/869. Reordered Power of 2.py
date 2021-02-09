from collections import Counter
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        power = 1
        Ncounter = Counter(str(N))
        for i in range(31):
            if Ncounter==Counter(str(power)): return True
            power = power<<1
        return False