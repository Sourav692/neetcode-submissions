class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {")":"(","}":"{","]":"["}
        stack = []

        for elem in s:
            if elem in closeToOpen:
                if stack and stack[-1] == closeToOpen[elem]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(elem)
        
        return True if not stack else False
        
        