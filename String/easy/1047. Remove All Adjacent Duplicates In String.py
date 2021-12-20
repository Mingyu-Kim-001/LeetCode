class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            c = s[i]
            if not stack or stack[-1] != c:
                stack.append(c)
            else:
                stack.pop()
            i += 1
        return "".join(stack)