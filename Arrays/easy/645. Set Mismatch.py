class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        isIn = [False]*(n+1)
        result = []
        for num in nums:
            if isIn[num]:
                result.append(num)
            isIn[num] = True
        for i in range(1,n+1):
            if not isIn[i]:
                result.append(i)
                break
        return result