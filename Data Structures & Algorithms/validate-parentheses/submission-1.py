class Solution:
    def isValid(self, s: str) -> bool:
        dct = {'{':'}', '(':')', '[':']'}
        stack = []
        for char in s :
            if char in dct:
                stack.append(char)
            elif len(stack) == 0 or dct[stack.pop()] != char:
                return False
        return len(stack)==0
        