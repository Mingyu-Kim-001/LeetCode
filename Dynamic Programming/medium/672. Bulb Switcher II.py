class Solution:
    def flipLights(self, n: int, m: int) -> int:
        flips = [1 + (1<<1) + (1<<2) + (1<<3) + (1<<4) + (1<<5),
                 1 + (1<<2) + (1<<4),
                 (1<<1) + (1<<3) + (1<<5),
                 (1) + (1<<3)
                ]
        mask = (1<<n) - 1 if n < 6 else (1<<6) - 1
        prev_state = set([0])
        for i in range(m):
            cur_state = set()
            for j in prev_state:
                for flip in flips:
                    new_state = (j ^ flip) & mask
                    cur_state.add(new_state)
            prev_state = cur_state
        return len(prev_state)