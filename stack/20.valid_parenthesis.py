


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        valid_parenthesis_map = {"]":"[", "}":"{", ")":"("}
        stack = []

        for c in s:
            if c in valid_parenthesis_map:

                if stack and stack[-1] == valid_parenthesis_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
            
        return len(stack) == 0


sol = Solution()

print(sol.isValid("()"))