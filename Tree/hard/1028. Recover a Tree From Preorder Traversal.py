class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        idx = 0
        while idx<len(S) and S[idx]!="-":
            idx+=1
        num = int(S[0:idx])
        root = TreeNode(num)
        stack = [[root,1]]
        while idx<len(S):
            if S[idx]=="-":
                start_hypen = idx
                while idx<len(S) and S[idx]=="-":
                    idx+=1
                hypen_count = idx-start_hypen
                
            start_int = idx
            while idx<len(S) and S[idx]!="-":
                idx+=1
            num = int(S[start_int:idx])
            #print(num,hypen_count)
            while stack and stack[-1][1]!=hypen_count:
                stack.pop()
            if not stack[-1][0].left:
                stack[-1][0].left = TreeNode(num)
                stack.append([stack[-1][0].left,stack[-1][1]+1])
            else:
                stack[-1][0].right = TreeNode(num)
                stack.append([stack[-1][0].right,stack[-1][1]+1])
            #print(stack)
        #print(root.val)
        return root