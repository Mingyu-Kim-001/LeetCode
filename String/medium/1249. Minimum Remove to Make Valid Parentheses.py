#Time: O(n)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        p_index_stack = []
        put_in_result = [False]*len(s)
        result = ""
        for i,c in enumerate(s):
            if c =="(":
                p_index_stack.append(i)
            elif c==")":
                if not p_index_stack: continue
                else:
                    put_in_result[p_index_stack.pop()] = True
                    put_in_result[i] = True
            else:
                put_in_result[i] = True
        for i,is_put in enumerate(put_in_result):
            if is_put: result+=s[i]
        return result