class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        flips = sum([1 if i=="0" else 0 for i in S])
        minFlips = flips
        for i in range(len(S)):
            if S[i]=="0":
                flips-=1
                if minFlips>flips: minFlips = flips
                
            else:
                flips+=1
        return minFlips