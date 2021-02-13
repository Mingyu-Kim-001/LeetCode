from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        if len(c1)!=len(c2):
            return False
        for i,j in zip(sorted(c1.values()),sorted(c2.values())):
            if i!=j:
                return False
        for i,j in zip(sorted(c1),sorted(c2)):
            if i!=j:
                return False
        return True