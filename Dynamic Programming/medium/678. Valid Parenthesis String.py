#Time: O(n)
class Solution:
    def checkValidString(self, s: str) -> bool:
        min_stack = max_stack = 0
        for c in s:
            if c == "*":
                min_stack = max(0,min_stack-1)
                max_stack = max_stack + 1
            elif c == "(":
                min_stack += 1
                max_stack += 1
            else:
                min_stack = max(0,min_stack-1)
                max_stack -= 1
            if max_stack < 0:
                return False
        return min_stack == 0