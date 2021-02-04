#Time: O(n)
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        bfs = deque([[beginWord,1]])
        wordSet = set(wordList)
        visit = set([beginWord])
        while bfs:
            curWord,curPathLen = bfs.popleft()
            if curWord==endWord: return curPathLen
            for i in range(len(curWord)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    changed = curWord[:i] + c + curWord[i+1:]
                    if not changed in visit and changed in wordSet:
                        visit.add(changed)
                        bfs.append([changed,curPathLen+1])
        return 0





#DFS, but time limit exceeded

# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         shortest = float("inf")
#         visit = set()
#         wordSet = set(wordList)
#         def DFS(curWord,wordCount):
#             # print(curWord,wordCount)
#             nonlocal shortest
#             if curWord == endWord:
#                 shortest = min(shortest,wordCount)
#                 return
#             if shortest<=wordCount:
#                 return
#             visit.add(curWord)
#             for i in range(len(curWord)):
#                 for c in "abcdefghijklmnopqrstuvwxyz":
#                     changed = curWord[:i] + c + curWord[i+1:]
#                     if changed in wordSet and not changed in visit:
#                         DFS(changed,wordCount+1)
#             visit.remove(curWord)
#         DFS(beginWord,1)
#         return shortest if shortest!=float("inf") else 0