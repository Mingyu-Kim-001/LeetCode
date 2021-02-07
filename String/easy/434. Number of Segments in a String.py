class Solution:
    def countSegments(self, s: str) -> int:
        splitted = s.split(" ")
        return sum([1 if i!="" else 0 for i in splitted])