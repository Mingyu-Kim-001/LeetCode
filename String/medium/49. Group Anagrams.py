#Time: O(n)
from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        tuple_to_index = {}
        for word in strs:
            counter = Counter(word)
            counter_to_tuple = []
            for c in "abcdefghijklmnopqrstuvwxyz":
                if not c in counter: counter_to_tuple.append(0)
                else: counter_to_tuple.append(counter[c])
            if not tuple(counter_to_tuple) in tuple_to_index:
                result.append([word])
                tuple_to_index[tuple(counter_to_tuple)] = len(result)-1
            else:
                result[tuple_to_index[tuple(counter_to_tuple)]].append(word)
        return result