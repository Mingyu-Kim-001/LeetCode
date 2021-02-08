class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        def findIndexInPieces(n):
            for i,piece in enumerate(pieces):
                if piece[0]==n:
                    return i
            return -1
        i = 0
        while i<len(arr):
            idx = findIndexInPieces(arr[i])
            if idx==-1:return False
            for piece_num in pieces[idx]:
                if piece_num!=arr[i]:return False
                i+=1
        return True