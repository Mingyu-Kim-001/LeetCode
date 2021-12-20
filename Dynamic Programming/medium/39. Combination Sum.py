class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target+1)]
        dp[0].append([])
        
        for cand in candidates:
            for i in range(1,target+1):
                if i - cand >= 0:
                    for comb in dp[i-cand]:
                        dp[i].append(comb+[cand])
        return dp[target]