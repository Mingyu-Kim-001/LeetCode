class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = pow(10,9)+7
        bridge_index = []
        i1 = 0
        i2 = 0
        partSum1 = partSum2 = 0
        maxSum = 0
        while i1<len(nums1) and i2<len(nums2):
            if nums1[i1]<nums2[i2]:
                partSum1+=nums1[i1]
                i1+=1
            elif nums1[i1]>nums2[i2]:
                partSum2+=nums2[i2]
                i2+=1
            else:
                maxSum+= max(partSum1,partSum2) + nums1[i1]
                partSum1 = partSum2 = 0
                i1+=1
                i2+=1
                
        while i1<len(nums1):
            partSum1+=nums1[i1]
            i1+=1
        while i2<len(nums2):
            partSum2+=nums2[i2]
            i2+=1
        maxSum+= max(partSum1,partSum2)
        return maxSum%MOD