import collections
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0;
        
        q = collections.deque()
        
        for c in s:
            
            if c not in q:
                q.append(c)
            else:
                
                index = q.index(c) + 1
                
                for i in range(index):
                    q.popleft()
                
                q.append(c)
            
            max_len = max(max_len, len(q))

            
        return max_len