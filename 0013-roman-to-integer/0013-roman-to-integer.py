class Solution:
    def romanToInt(self, s: str) -> int:
        
        sum = 0
        while len(s) > 0:
            if "CM" in s:
                s = s.replace("CM", "", 1)
                sum += 900
            elif "CD" in s:
                s = s.replace("CD", "", 1)
                sum += 400
            elif "XC" in s:
                s = s.replace("XC", "", 1)
                sum += 90
            elif "XL" in s:
                s = s.replace("XL", "", 1)
                sum += 40
            elif "IX" in s:
                s = s.replace("IX", "", 1)
                sum += 9
            elif "IV" in s:
                s = s.replace("IV", "", 1)
                sum += 4
            elif "M" in s:
                s = s.replace("M", "", 1)
                sum += 1000
            elif "D" in s:
                s = s.replace("D", "", 1)
                sum += 500
            elif "C" in s:
                s = s.replace("C", "", 1)
                sum += 100
            elif "L" in s:
                s = s.replace("L", "", 1)
                sum += 50
            elif "X" in s:
                s = s.replace("X", "", 1)
                sum += 10
            elif "V" in s:
                s = s.replace("V", "", 1)
                sum += 5
            elif "I" in s:
                s = s.replace("I", "", 1)
                sum += 1
                    
                    
        return sum
