from collections import defaultdict
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        idx_of_char = defaultdict(list)
        for idx, char in enumerate(ring):
            idx_of_char[char].append(idx)
        cur_idx_and_moves = {0:0}
        for char in key:
            temp = defaultdict(lambda : float("inf"))
            for next_idx in idx_of_char[char]:
                for cur_idx, cur_move in cur_idx_and_moves.items():
                    temp[next_idx] = min(temp[next_idx], abs(cur_idx - next_idx) + cur_move + 1, len(ring) - abs(cur_idx - next_idx) + cur_move + 1)
            cur_idx_and_moves = temp
        return min(cur_idx_and_moves.values())