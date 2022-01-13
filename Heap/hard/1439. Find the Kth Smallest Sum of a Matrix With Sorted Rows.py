import heapq as hq
class Solution:
    def k_smallest_from_pair(self, l1, l2, k):
        heap = [[l1[0] + l2[0], 0, 0]]
        res = []
        seen = set()
        while heap and len(res) < k:
            current_smallest, i, j = hq.heappop(heap)
            res.append(current_smallest)
            if i < len(l1) - 1 and (i + 1, j) not in seen:
                hq.heappush(heap, [l1[i + 1] + l2[j], i + 1, j])
                seen.add((i + 1, j))
            if j < len(l2) - 1 and (i, j + 1) not in seen:
                hq.heappush(heap, [l1[i] + l2[j + 1], i, j + 1])
                seen.add((i, j + 1))
        return res
        
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m, n = len(mat), len(mat[0])
        res = mat[0]
        for row in mat[1:]:
            res = self.k_smallest_from_pair(res, row, k)
        return res[-1]