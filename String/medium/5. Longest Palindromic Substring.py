# Time: O(n^2), Space: O(n)
class Solution(object):
    def longestPalindrome(self, s):
        if len(s)==1:
            return s
        maxlen = 0
        result = ""
        for i in range(len(s)):
            l,r = i-1,i
            while l>=0 and r<=len(s)-1:
                if s[l]!=s[r]:
                    if maxlen<2*(r-i):
                        maxlen = 2*(r-i)
                        result = s[l+1:r]
                    break
                l,r = l-1,r+1
            else:
                if maxlen<2*(r-i):
                    maxlen = 2*(r-i)
                    result = s[l+1:r]
                
            l,r = i-1,i+1
            while l>=0 and r<=len(s)-1:
                if s[l]!=s[r]:
                    if maxlen<2*(r-i)-1:
                        maxlen = 2*(r-i)-1
                        result = s[l+1:r]
                    break
                l,r = l-1,r+1
            else:
                if maxlen<2*(r-i)-1:
                    maxlen = 2*(r-i)-1
                    result = s[l+1:r]
                
        if maxlen == 0:
            result = s[0]
        return result