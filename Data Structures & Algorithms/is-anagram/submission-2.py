class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) == 0 or len(t) == 0:
            return False

        if len(s) != len(t):
            return False
        
        tracker = [0]*26

        for i in range(len(s)):
            tracker[ord(s[i])-ord("a")] += 1
            tracker[ord(t[i])-ord("a")] -= 1
        
        for i in tracker:
            if i != 0:
                return False
        
        return True
