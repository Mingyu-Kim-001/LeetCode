class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        consecutive_len = [0,0]
        ans = 0
        for i,c in enumerate(s):
            c = ord(c) - ord("0")
            if i == 0 or s[i] == s[i-1]:
                consecutive_len[c] += 1
            else:
                consecutive_len[c] = 1
                
            if consecutive_len[c^1] >= consecutive_len[c]:
                ans += 1
        return ans