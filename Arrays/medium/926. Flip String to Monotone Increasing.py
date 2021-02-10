#Time: O(n)
class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        n_zero = n_one = 0
        for c in S:
            if c=="0":n_zero+=1
            else:n_one+=1
        cur_n_zero = cur_n_one = 0
        result = n_zero
        for c in S:
            if c=="0":cur_n_zero+=1
            else:cur_n_one+=1
            result = min(result,cur_n_one + n_zero - cur_n_zero)
        return result