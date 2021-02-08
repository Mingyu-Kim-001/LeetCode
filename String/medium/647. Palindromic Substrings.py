#Time: O(n)
class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            l = r = i
            while l>=0 and r<len(s) and s[l]==s[r]: #count palindrom of odd length. 
                l,r = l-1,r+1
                result+=1
            l,r = i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]: #count palindrom of even length. 
                l,r = l-1,r+1
                result+=1
        return result