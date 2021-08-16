class Solution:
    def minWindow(self, s: str, t: str) -> str:
        remaining = {}
        for char in t:
            if not char in remaining:
                remaining[char] = 1
            else:
                remaining[char] += 1
        
        reached = sum(remaining.values()) # if reached == 0: window contains t
        l = r = 0
        ans = (0,float("inf"))
        
        while r < len(s):
            # print(l,r, s[r], remaining, reached)
            
            if s[r] in remaining:
                if remaining[s[r]] > 0:
                    reached -= 1
                remaining[s[r]] -= 1
                    
            if reached == 0:
                while l <= r:
                    if s[l] in remaining:
                        if remaining[s[l]] == 0:
                            break
                        else:
                            remaining[s[l]] += 1
                    l += 1
                    
                if ans[1] - ans[0] > r - l:
                    ans = (l, r)
                    
            r += 1
            
        return s[ans[0]:ans[1]+1] if ans[1] < float("inf") else ""