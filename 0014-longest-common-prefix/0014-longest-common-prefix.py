class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for i, ch in enumerate(strs[0]):
            for s in strs[1:]:
                if i >= len(s) or s[i] != ch:
                    return result
            result = result + ch
                
        return result