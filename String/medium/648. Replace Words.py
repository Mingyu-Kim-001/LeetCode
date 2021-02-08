class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        #dictionary = ["abc","def","acf"]
        dic_trie = {}
        for root in dictionary:
            cur_trie = dic_trie
            for c in root:
                if not c in cur_trie:
                    cur_trie[c] = {}
                cur_trie = cur_trie[c]
            cur_trie["end"] = root
        words = sentence.split(" ")
        result_list = []
        for word in words:
            cur_trie = dic_trie
            for c in word:
                if not c in cur_trie:
                    result_list.append(word)
                    break
                cur_trie = cur_trie[c]
                if "end" in cur_trie:
                    result_list.append(cur_trie["end"])
                    break
            else:
                result_list.append(word)
        return " ".join(result_list)