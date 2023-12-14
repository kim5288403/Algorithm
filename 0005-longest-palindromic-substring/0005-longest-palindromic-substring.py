class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_s, max_e = 0, 0
        
        for i in range(len(s)):
            
            start, end = i, i
            while 0 <= start and len(s) > end and s[start] == s[end]:
                if max_e - max_s < end - start:
                    max_s, max_e = start, end
                start, end = start - 1, end + 1
                
            start, end = i, i + 1
            while 0 <= start and len(s) > end and s[start] == s[end]:
                if max_e - max_s < end - start:
                    max_s, max_e = start, end
                start, end = start - 1, end + 1
            
   
        return s[max_s : max_e + 1]


