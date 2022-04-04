class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        queue = [[]]
        for num in range(1, n+2):
            queue2 = []
            for comb in queue:
                #When putting all the remaining numbers isn't sufficient
                if len(comb) + n - num + 1 < k:
                    continue
                #When the length of combination is k
                elif len(comb) == k:
                    ans.append(comb)
                #else recursively add nums
                else:
                    queue2.append(comb)
                    queue2.append(comb+[num])
            queue = queue2
        return ans