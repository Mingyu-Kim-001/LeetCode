#Time:O(n)
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:return []
        start = end = None
        result = []
        for i,num in enumerate(nums):
            if start==None:
                start = end = num
            else:
                if num==nums[i-1]+1:
                    end = num
                else:
                    if start==end:
                        result.append(str(start))
                    else:
                        result.append(str(start)+"->"+str(end))
                    start = end = num
        if start==end:
            result.append(str(start))
        else:
            result.append(str(start)+"->"+str(end))
        return result