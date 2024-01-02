class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        pnlist = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        result = []
        
        def dfs(index, string = ""):
            
            if len(string) == len(digits):
                if digits:
                    result.append(string)
                return
            for i in pnlist[digits[index]]:
                dfs(index + 1, string + i)
                
                
        dfs(0)
        
        return result
        
            