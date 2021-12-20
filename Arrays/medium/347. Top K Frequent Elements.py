#Time: O(n)
from collections import Counter,defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counter = Counter(nums)
        freqBucket = defaultdict(list)
        for num,freq in counter.items():
            freqBucket[freq].append(num)
        result = []
        count = 0
        for i in range(n,0,-1):
            if i in freqBucket:
                result+= freqBucket[i]
                count+= len(freqBucket[i])
            if count>=k:
                return result