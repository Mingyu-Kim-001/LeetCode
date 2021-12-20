class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        first = s[:len(s)//2]
        second = s[len(s)//2:]
        first_vowel_count = second_vowel_count = 0
        
        for i in range(len(first)):
            if first[i] in "aeiouAEIOU":
                first_vowel_count += 1
            if second[i] in "aeiouAEIOU":
                second_vowel_count += 1
        
        return first_vowel_count == second_vowel_count
        