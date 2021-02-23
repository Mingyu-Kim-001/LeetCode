class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            for subset in result[:]:
                result.append(subset+[num])
        return result