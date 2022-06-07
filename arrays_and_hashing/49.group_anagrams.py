from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        words_map = defaultdict(list);

        for str in strs:
            
            str_count = 0
            for char in str:
                str_count += ord(char)
            
            words_map[str_count].append(str)
        
        print(words_map)

        return list(words_map.values())

sol = Solution()

print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))