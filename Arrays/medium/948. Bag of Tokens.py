class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        if not tokens: return 0
        tokens.sort()
        l,r = 0,len(tokens)-1
        score = 0
        while l<r:
            if tokens[l]<=P:
                P-=tokens[l]
                score+=1
                l+=1
            else:
                if score==0: return 0
                P+=tokens[r]
                score-=1
                r-=1
        if tokens[l]<=P: score+=1
        return score