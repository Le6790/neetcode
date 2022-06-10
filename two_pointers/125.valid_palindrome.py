import re
from tracemalloc import start

from numpy import true_divide
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_str = re.sub('[^a-z0-9]+','',s.lower())
        start = 0
        end = len(new_str)-1
        print("orig_str", s,"new_str",new_str)
        if (len(new_str) <=1):
            return True

        for i in range(0,len(new_str)):
            print(new_str[start])
            print(new_str[end])
            print("---")
            if new_str[start] != new_str[end]:
                return False
            start+=1
            end-=1
        
        return True

    def isPalindromeOptimized(self, s):

        l =0
        r = len(s)-1

        while l < r:
            while l < r and not self.isAlphaNumeric(s[l]):
                l+=1

            while l < r and not self.isAlphaNumeric(s[r]):
                r-=1
            
            #print(s[l],s[r])
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True

    def isAlphaNumeric(self,char):
        if (ord('a') <= ord(char) <= ord('z') or
        ord('A') <= ord(char) <= ord('Z') or
        ord('0') <= ord(char) <= ord('9')
        ): 
            return True
        
        return False
solution = Solution()

print(solution.isPalindromeOptimized("A man, a plan, a canal: Panama"))
print(solution.isPalindrome("0P"))