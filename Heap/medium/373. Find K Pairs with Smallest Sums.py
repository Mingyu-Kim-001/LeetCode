import heapq as hq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = [[nums1[0] + nums2[0], 0, 0]]
        seen = set([(0,0)])
        ans = []
        while k > 0 and heap:
            _, i, j = hq.heappop(heap)
            ans.append([nums1[i],nums2[j]])
            if i + 1 < len(nums1) and not (i + 1, j) in seen:
                hq.heappush(heap, [nums1[i + 1] + nums2[j], i + 1, j])
                seen.add((i + 1, j))
            if j + 1 < len(nums2) and not (i, j + 1) in seen:
                hq.heappush(heap, [nums1[i] + nums2[j + 1], i, j + 1])
                seen.add((i, j + 1))
            k -= 1
        return ans