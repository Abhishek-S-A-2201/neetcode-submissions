class Solution:
    def isValid(self, s: str) -> bool:
        
        parentheses = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        stack = []

        for i in s:
            if i in parentheses:
                if len(stack) == 0:
                    return False
                
                if parentheses[i] != stack.pop():
                    return False
                
            else:
                stack.append(i)
        
        if len(stack) == 0:
            return True
        else:
            return False