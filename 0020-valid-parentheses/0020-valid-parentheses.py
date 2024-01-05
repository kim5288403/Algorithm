class Solution:
    def isValid(self, s: str) -> bool:
        key = {"(" : ")", "[" : "]", "{" : "}"}
        stack = []
        
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            elif not stack or c != key[stack.pop()]:
                return False        
        
        return not stack
            
            
        