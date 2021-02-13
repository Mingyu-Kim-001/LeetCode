class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        result = []
        for i,num in enumerate(nums):
            while result and result[-1]>num and k-len(result)+1<=len(nums)-i:
                result.pop()
            if len(result)<k:
                result.append(num)
        return result