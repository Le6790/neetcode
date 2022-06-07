from collections import defaultdict


class Solution(object):

    def groupAnagrams(self,strs):

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 #list of a-z

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            res[tuple(count)].append(s)
        
        return res.values()

    def groupAnagramsUsingSort(self,strs):

        res = defaultdict(list)

        for s in strs:
            sorted_s = sorted(s)
            res[tuple(sorted_s)].append(s)
        return res.values()

sol = Solution()

print(sol.groupAnagrams(["ac","c"]))
print("----")
print(sol.groupAnagramsUsingSort(["ac","c"]))