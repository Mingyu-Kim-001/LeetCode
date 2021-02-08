class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        for i in S:
            if i=="(":
                stack.append(0)
            else:
                if stack[-1]==0:
                    stack[-1] = 1
                    if len(stack)>1 and stack[-2]!=0:
                        stack.pop()
                        stack[-1]+=1
                else:
                    score = stack.pop()
                    stack[-1] = score*2
                    if len(stack)>1 and stack[-2]!=0:
                        score = stack.pop()
                        stack[-1]+= score
        return stack[0]