class Solution:
    def minFlips(self, target: str) -> int:
        flip_count = 0
        for i in range(len(target)):
            if target[i] == "0":
                if flip_count % 2 == 1:
                    flip_count += 1
            else:
                if flip_count % 2 == 0:
                    flip_count += 1
        return flip_count