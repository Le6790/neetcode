from numpy import diff, true_divide


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        
        s_dict,t_dict = {}, {}

        for i in range(0,len(s)):
            s_dict[s[i]] = 1 + s_dict.get(s[i],0)
            t_dict[t[i]] = 1 + t_dict.get(t[i],0)

        for c in s_dict:
            if s_dict[c] != t_dict.get(c, 0):
                return False
            

        return True

    def isAnagram2(self, s, t):
        s_sorted = sorted(s)
        t_sorted = sorted(t)
        
        if s_sorted == t_sorted:
            return True
        return False
        
sol = Solution()
print(sol.isAnagram2("anagram","nagaram")) # True
# print(sol.isAnagram("rat","cat"))
print(sol.isAnagram2("a","ab")) # False