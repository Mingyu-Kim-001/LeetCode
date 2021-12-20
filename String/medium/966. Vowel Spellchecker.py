import re
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        
        def vowel_to_1(s):
            return re.sub("[aeiou]","1",s.lower())
        
        word_set = set(wordlist)
        lower_to_org = {}
        vowel_to_1_dict = {}
        for word in wordlist:
            if not word.lower() in lower_to_org:
                lower_to_org[word.lower()] = word  
            if not vowel_to_1(word) in vowel_to_1_dict:
                vowel_to_1_dict[vowel_to_1(word)] = word
                
        result = []
        for query in queries:
            if query in word_set:
                result.append(query)
            elif query.lower() in lower_to_org:
                result.append(lower_to_org[query.lower()])
            elif vowel_to_1(query) in vowel_to_1_dict:
                result.append(vowel_to_1_dict[vowel_to_1(query)])
            else:
                result.append("")
                
        return result