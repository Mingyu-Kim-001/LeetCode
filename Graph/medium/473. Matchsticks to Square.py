class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4:
            return False
        if sum(matchsticks) % 4:
            return False
        matchsticks.sort(reverse=True)
        if matchsticks[0] > sum(matchsticks) // 4:
            return False
        
        def DFS(targets, matchsticks, matchstick_idx):
            seen_length = set()
            if matchstick_idx == len(matchsticks):
                return True
            for i, target in enumerate(targets):
                if not target in seen_length and matchsticks[matchstick_idx] <= target:
                    targets[i] -= matchsticks[matchstick_idx]
                    if DFS(targets, matchsticks, matchstick_idx+1):
                        return True
                    targets[i] += matchsticks[matchstick_idx]
                seen_length.add(target)
            return False
        
        return DFS([sum(matchsticks) // 4] * 4, matchsticks, 0)
        
