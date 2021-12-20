#Time:O(n^2)
from collections import defaultdict
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i):
                product[nums[i]*nums[j]]+=1
        result = 0
        for i in product:
            result+=4*product[i]*(product[i]-1)
        return result