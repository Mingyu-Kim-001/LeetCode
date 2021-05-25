from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        file_by_content = defaultdict(list)
        for path in paths:
            path_split = path.split(" ")
            directory = path_split[0]
            for file_and_content in path_split[1:]:
                file, content = file_and_content.split("(")
                file_by_content[content].append(directory+"/"+file)
        return [files for files in file_by_content.values() if len(files) > 1]