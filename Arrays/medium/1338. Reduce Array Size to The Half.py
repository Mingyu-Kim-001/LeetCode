from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = Counter(arr)
        removed_count = 0
        removed_num = 0
        for num in sorted(counter, key=lambda x: counter[x], reverse=True):
            removed_count += counter[num]
            removed_num += 1
            if removed_count >= len(arr) // 2:
                return removed_num
                