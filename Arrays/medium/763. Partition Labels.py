#Time: O(n), Space: O(n)
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        i = 0
        result = []
        while i < len(S):
            start = i
            j = len(S) - 1
            end = i + 1
            while i < end:
                j = len(S) - 1
                c = S[i]
                while j >= end:
                    if c == S[j]:
                        break
                    j -= 1
                end = max(end,j+1)
                i += 1
            result.append(end-start)
        return result