class Solution:
    def isPalindrome(self, x: int) -> bool:
        result = True
            
        if x < 0:
            return False
        
        s = str(x)
        
        l = 0
        r = 0
        if len(s) % 2 == 0:
            if s[len(s) // 2] != s[len(s) // 2 - 1]:
                return False
            else:
                l, r = (len(s) // 2) - 2, (len(s) // 2) + 1
                while l >= 0 and r < len(s):
                    if s[l] != s[r]:
                        return False
                        break
                    l -= 1
                    r += 1
        else:
            
            l, r = (len(s) // 2) - 1, (len(s) // 2) + 1
            
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    return False
                    break
                l -= 1
                r += 1
                
        
        return True        