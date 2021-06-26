class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        whole = [[] for _ in range(n+1)]
        total = [[] for _ in range(n+1)]
        whole[1].append("()")
        total[1].append("()")
        for i in range(2,n+1):
            whole[i] = ["(" + p + ")" for p in total[i-1]]
            total[i] += whole[i]
            for j in range(1,i):
                for p1 in whole[j]:
                    for p2 in total[i-j]:
                        total[i].append(p1+p2)
        return total[n]