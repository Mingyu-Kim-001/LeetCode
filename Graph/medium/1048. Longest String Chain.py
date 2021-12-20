from collections import deque, defaultdict
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words_by_len = defaultdict(set)
        for word in words:
            words_by_len[len(word)].add(word)
        bfs = deque()
        ans = 0
        
        for i in sorted(words_by_len):
            for word in words_by_len[i]:
                bfs.append([word,1])
            
            bfs2 = deque()
            
            while bfs:
                word,chain_len = bfs.popleft()
                ans = max(ans, chain_len)
                for j in range(len(word)+1):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        new_word = word[:j] + c + word[j:]
                        if new_word in words_by_len[len(word)+1]:
                            words_by_len[len(word)+1].remove(new_word)
                            bfs2.append([new_word,chain_len+1])
            bfs = bfs2
            
        return ans