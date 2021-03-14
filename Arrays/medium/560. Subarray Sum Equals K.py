#Time: O(n)
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixes = defaultdict(int)
        prefix = result = 0
        prefixes[0] = 1
        for num in nums:
            prefix += num
            if prefix - k in prefixes:
                result += prefixes[prefix-k]
            prefixes[prefix] += 1
        return result