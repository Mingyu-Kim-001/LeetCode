# Time: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {")":"(","]":"[","}":"{"}
        for c in s:
            if c in pair:
                if len(stack)==0 or stack[-1]!=pair[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return len(stack)==0