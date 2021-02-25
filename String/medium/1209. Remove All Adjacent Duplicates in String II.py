#Time: O(n)
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i,c in enumerate(s):
            if not stack or stack[-1][0]!=c:
                stack.append(c)
            elif stack[-1][0]==c:
                if len(stack[-1])==k-1:
                    stack.pop()
                else:
                    stack[-1]+=c
        return "".join(stack)