#Time: O(n)
class Solution:
    def longestPrefix(self, s: str) -> str:
        j = 0
        table = [0]*len(s)
        for i in range(1,len(s)):
            while j>0 and s[i]!=s[j]:
                j = table[j-1]
            if s[i] == s[j]:
                j+=1
                table[i] = j
        return s[:table[len(s)-1]]
        