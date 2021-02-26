#Time: O(n)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        totalLen = len(nums1) + len(nums2)
        l = r = 0
        prev = cur = None
        while l+r<=(totalLen//2):
            prev = cur
            if l>=len(nums1):
                cur = nums2[r]
                r+=1
            elif r>=len(nums2):
                cur = nums1[l]
                l+=1
            elif nums1[l]<nums2[r]:
                cur = nums1[l]
                l+=1
            else:
                cur = nums2[r]
                r+=1
        if totalLen%2==1:
            return cur
        return (prev+cur)/2