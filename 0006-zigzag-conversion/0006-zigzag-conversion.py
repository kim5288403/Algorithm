class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        result = []
        
        for i in range(numRows):
            result.append('')
        
        if numRows == 1:
            return s
        else:
            
            for i in range(len(s)):
                modnum = numRows - 1
                
                if i % (modnum * 2) < modnum:
                    result[i % modnum] += s[i]
                else:
                    result[modnum - i % modnum] += s[i]
        
        
        return ''.join(result)
            
            