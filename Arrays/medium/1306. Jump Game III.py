class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True
        visited = set([start])
        new_visited = set([start])
        while new_visited:
            next_new_visited = set()
            for idx in new_visited:
                if idx + arr[idx] < len(arr) and idx + arr[idx] not in visited:
                    visited.add(idx + arr[idx])
                    next_new_visited.add(idx + arr[idx])
                    if arr[idx+arr[idx]] == 0:
                        return True
                if 0 <= idx - arr[idx] and idx - arr[idx] not in visited:
                    visited.add(idx - arr[idx])
                    next_new_visited.add(idx - arr[idx])
                    if arr[idx-arr[idx]] == 0:
                        return True
            new_visited = next_new_visited
        return False
            