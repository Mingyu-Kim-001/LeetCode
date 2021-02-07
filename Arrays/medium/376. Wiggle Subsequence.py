class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums)==0: return 0
        if len(nums)==1: return 1
        isFirst = True
        isAscending = False
        result = [nums[0]]
        for num in nums[1:]:
            if result[-1]==num:continue
            if isFirst:
                isAscending = result[-1]<num
                result.append(num)
                isFirst = False
            elif isAscending:
                if result[-1]<num:
                    result[-1]=num
                else:
                    result.append(num)
                    isAscending=False
            else:
                if result[-1]>num:
                    result[-1] = num
                else:
                    result.append(num)
                    isAscending=True
        return len(result)