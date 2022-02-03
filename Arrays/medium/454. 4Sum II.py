from collections import defaultdict
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        for nums in [nums1, nums2, nums3, nums4]:
            nums.sort()
        two_sums = defaultdict(int)
        for num1 in nums1:
            for num2 in nums2:
                two_sums[num1 + num2] += 1
        
        ans = 0
        for num3 in nums3:
            for num4 in nums4:
                if -num3 - num4 in two_sums:
                    ans += two_sums[-num3-num4]
        return ans