#Time: O(n), extra space(without output list):O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        length = len(nums)
        for num in nums:
            prefix.append(prefix[-1]*num)
        for num in nums[::-1]:
            suffix.append(suffix[-1]*num)
        outputs = [prefix[i]*suffix[length-1-i] for i in range(length)]
        return outputs