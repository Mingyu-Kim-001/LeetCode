class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans_reverse = []
        for i, arr in enumerate(nums):
            for j, num in enumerate(arr):
                if len(ans_reverse) <= i + j:
                    ans_reverse.append([])
                ans_reverse[i+j].append(num)
        return [num for arr in ans_reverse for num in arr[::-1]]