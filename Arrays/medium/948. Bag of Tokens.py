from collections import deque
class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens_deque = deque(sorted(tokens))
        S = 0
        while tokens_deque:
            while tokens_deque and P>=tokens_deque[0]:
                P-=tokens_deque.popleft()
                S+=1
            if len(tokens_deque)<=1: break
            if S>0:
                S-=1
                P+=tokens_deque.pop()
            if S==0 and P<tokens_deque[0]:
                break
        return S