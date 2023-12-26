class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        
        while num > 0:
            if num >= 1000:
                num -= 1000
                result = result + "M"
            elif num >= 900:
                num -= 900
                result = result + "CM"
            elif num >= 500:
                num -= 500
                result = result + "D"
            elif num >= 400:
                num -= 400
                result = result + "CD"
            elif num >= 100:
                num -= 100
                result = result + "C"
            elif num >= 90:
                num -= 90
                result = result + "XC"
            elif num >= 50:
                num -= 50
                result = result + "L"
            elif num >= 40:
                num -= 40
                result = result + "XL"
            elif num >= 10:
                num -= 10
                result = result + "X"
            elif num >= 9:
                num -= 9
                result = result + "IX"
            elif num >= 5:
                num -= 5
                result = result + "V"
            elif num >= 4:
                num -= 4
                result = result + "IV"
            else:
                num -= 1
                result = result + "I"
        
        return result


        