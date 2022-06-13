class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1
        l= 0
        r = 0
        #print(s)
        substring = set()
        longest_substring = 0
        
        while r < len(s):
            #print("substring:",substring)
            while s[r] in substring:
                substring.remove(s[l])
                l+=1
                
            substring.add(s[r])
                
            r +=1
            longest_substring = max(longest_substring,r-l)
        return longest_substring

    def lengthOfLongestSubstring_neetcode(self, s):
        charSet = set()

        l = 0
        r = 1
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l +=1
            charSet.add(s[r])
            res = max(res, (r-l)+1)

        return res

solution = Solution()

print(solution.lengthOfLongestSubstring('abcabcbb'))
print(solution.lengthOfLongestSubstring('bbbbb'))
print(solution.lengthOfLongestSubstring('pwwkew'))
print(solution.lengthOfLongestSubstring('aa'))
print(solution.lengthOfLongestSubstring('au'))

print("---")
print(solution.lengthOfLongestSubstring_neetcode('abcabcbb'))
print(solution.lengthOfLongestSubstring_neetcode('bbbbb'))
print(solution.lengthOfLongestSubstring_neetcode('pwwkew'))
print(solution.lengthOfLongestSubstring_neetcode('aa'))
print(solution.lengthOfLongestSubstring_neetcode('au'))

