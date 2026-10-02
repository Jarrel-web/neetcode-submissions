class Solution:
    def isValid(self, s: str) -> bool:
        validParenthesePair = {
            '}':'{',
            ']':'[',
            ')':'('
        }
        stack = []
        for char in s:
            if char in validParenthesePair:
                if stack and stack[-1] == validParenthesePair[char]:
                    stack.pop()
                else:
                    return False
            else:   
                stack.append(char)
        return True if not stack else False