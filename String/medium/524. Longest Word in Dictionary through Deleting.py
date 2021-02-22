#Time: O(MN), M<=1000 N<=1000
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        def match(s,dword):
            i1 = i2 = 0
            while i1<len(s) and i2<len(dword):
                if s[i1] == dword[i2]:
                    i2+=1
                i1+=1
            return i2==len(dword)
        # d.sort(key=lambda x:(-len(x),x))
        matched = []
        for dword in d:
            if len(dword)>len(s): continue
            if match(s,dword): matched.append(dword)
        return min(matched,key=lambda x:(-len(x),x)) if matched else ""