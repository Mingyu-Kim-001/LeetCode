#Time: O(n)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gain = [gas[i] - cost[i] for i in range(len(gas))]
        gain_extended = gain*2
        prefix = len_sequence = 0
        print(gain_extended)
        for i,num in enumerate(gain_extended):
            prefix+=num
            print(i,prefix)
            if prefix<0:
                prefix = len_sequence = 0
            else:
                len_sequence+=1
                if len_sequence==len(gas):
                    return i-len_sequence+1
        return -1