#Time: O(n) Space: O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1
        seen = set()
        maxLen = 0
        while r<=len(s):
            if s[r-1] in seen:
                while l<r and s[l]!=s[r-1]:
                    seen.remove(s[l])
                    l+=1
                l+=1
            else:
                seen.add(s[r-1])
            maxLen = max(maxLen,r-l)
            r+=1
        return maxLen