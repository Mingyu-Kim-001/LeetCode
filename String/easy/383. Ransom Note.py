#Time: O(n)
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rCount = Counter(ransomNote)
        mCount = Counter(magazine)
        for c in rCount:
            if not c in mCount or mCount[c]<rCount[c]: return False
        return True