from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        return "".join([c * counter[c] for c in sorted(counter.keys(), key = lambda c:counter[c], reverse=True)])