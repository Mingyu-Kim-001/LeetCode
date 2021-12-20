from collections import Counter
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        word_counters = [Counter(word) for word in words]
        remaining = Counter(letters)
        
        def explore(word_idx, remaining):
            if word_idx >= len(word_counters):
                return 0
            word_counter = word_counters[word_idx]
            new_remaining = {char:count for char, count in remaining.items()}
            max_score_with_this_word = 0
            for char, count in word_counter.items():
                if not char in remaining or count > remaining[char]:
                    max_score_with_this_word = 0
                    break
                max_score_with_this_word += score[ord(char)-ord('a')] * count
                new_remaining[char] -= count
            else:
                max_score_with_this_word += explore(word_idx + 1, new_remaining)
            max_score_without_this_word = explore(word_idx + 1, remaining)
            return max(max_score_with_this_word, max_score_without_this_word)
                
        return explore(0, remaining)