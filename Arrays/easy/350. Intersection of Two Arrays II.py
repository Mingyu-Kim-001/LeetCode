from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_count = Counter(nums1)
        nums2_count = Counter(nums2)
        ans = []
        
        for num in nums1_count:
            if num in nums2_count:
                ans += [num] * min(nums1_count[num], nums2_count[num])
        
        return ans