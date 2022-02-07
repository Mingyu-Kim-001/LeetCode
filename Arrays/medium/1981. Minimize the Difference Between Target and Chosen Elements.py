class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        seen = set(mat[0])
        for row in mat[1:]:
            seen2 = set()
            for num in row:
                for existing_num in seen:
                    if existing_num + num < 2 * target:
                        seen2.add(existing_num + num)
            seen = seen2
        ans = float("inf")
        for num in seen:
            ans = min(abs(num - target), ans)
        return ans if ans != float("inf") else sum([min(row) for row in mat]) - target