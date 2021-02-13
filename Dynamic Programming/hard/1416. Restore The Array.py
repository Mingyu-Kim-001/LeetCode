class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        dp = [0]*(len(s)+1) # dp[i] : restore s[i:]
        dp[len(s)] = 1
        for i in range(len(s)-1,-1,-1):
            if s[i]=="0": continue #dp[i] = 0 in this case
            if int(s[i])>k: return 0
            cur_num = 0
            for j in range(i,len(s)):
                cur_num = 10*cur_num + int(s[j])
                if cur_num>k: break
                dp[i]+=dp[j+1]
        return dp[0]%(pow(10,9)+7)