
class Solution:
    def minSubarray(self, nums, p: int) -> int:

        largestIndex = {0:-1}
        minLen = float("inf")
        prev = 0
        remaining_of_total = sum(nums)%p
        if remaining_of_total==0: return 0
        for i,num in enumerate(nums):
            r = (prev+num)%p
            r_required = (r - remaining_of_total)%p
            largestIndex[r] = i
            #print(r,r_required,largestIndex)
            if r_required in largestIndex and minLen>i-largestIndex[r_required]:
                minLen = i-largestIndex[r_required]
            prev+=num
        return -1 if (minLen == float("inf") or minLen==len(nums)) else minLen