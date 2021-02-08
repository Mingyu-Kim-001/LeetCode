class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        prev = -2*k-1
        for i,num in enumerate(nums):
            if num==1:
                if i-prev<=k:
                    return False
                prev = i
        return True