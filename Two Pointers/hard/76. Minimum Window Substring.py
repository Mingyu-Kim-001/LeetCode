#Time:O(n)
from collections import Counter,defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l,r = 0,1
        tCounter = Counter(t)
        sCounter = defaultdict(int)
        tLen = len(t)
        total = 0
        resultLen = float("inf")
        result = ""
        while r<=len(s):
            if not s[r-1] in tCounter: 
                r+=1
                continue
            if tCounter[s[r-1]]>sCounter[s[r-1]]:
                total+=1
            sCounter[s[r-1]]+=1
            if total==tLen:
                while l<r and (not s[l] in sCounter or sCounter[s[l]]>tCounter[s[l]]):
                    if s[l] in sCounter:
                        sCounter[s[l]]-=1
                    l+=1
                if resultLen>r-l:
                    resultLen = r-l
                    result = s[l:r]
            r+=1
            
        return result