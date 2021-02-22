#Time:O(n)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        table = [0]*len(needle)
        j = 0
        for i in range(1,len(needle)):
            while j>0 and needle[i]!=needle[j]:
                j = table[j-1]
            if needle[i]==needle[j]:
                j+=1
                table[i] = j
        j = 0
        for i in range(len(haystack)):
            while j>0 and haystack[i]!=needle[j]:
                j = table[j-1]
            if haystack[i] == needle[j]:
                j+=1
            if j==len(needle): return i-len(needle)+1
        return -1