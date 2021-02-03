# Time: O(n^2)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n==0: return nums1
        i = j = 0
        while i<m+j and j<n:
            if nums1[i]>nums2[j]:
                nums1[i+1:] = nums1[i:-1]
                nums1[i] = nums2[j]
                j+=1
            i+=1
        if j<n: nums1[i:] = nums2[j:]