from collections import Counter
class Solution:
    def minSetSize(self, arr) -> int:
        counter = Counter(arr)
        counter = sorted(counter.items(),key=lambda x:x[1],reverse=True)
        total = 0
        result = 0
        for key,value in counter:
            total+=value
            result+=1
            if total>=len(arr)/2:
                return result