

import math
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        num_stack = []
        
        for tok in tokens:
            
            if tok not in ["*","+", "-", "/"]:
                num_stack.append(tok)

            
            if tok == "*":
                val1 = int(num_stack.pop())
                val2 = int(num_stack.pop())

                num_stack.append(val2*val1)

            elif tok == "+":
                val1 = int(num_stack.pop())
                val2 = int(num_stack.pop())

                num_stack.append(val2+val1)

            elif tok == "-":
                val1 = int(num_stack.pop())
                val2 = int(num_stack.pop())

                num_stack.append(val2-val1)
            
            elif tok == "/":
                val1 = int(num_stack.pop())
                val2 = int(num_stack.pop())

                num_stack.append(int(round(val2/val1)))
            
            print(num_stack, tok)
        
        return num_stack.pop()


solution = Solution()

print(solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))