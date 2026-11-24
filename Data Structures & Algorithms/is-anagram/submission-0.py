class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = dict()

        if len(s) != len(t):
            return False

        # for char in s:
        #     if char in letters:
        #         letters[char] = letters[char] + 1
        
        for char in t:
            if t.count(char) != s.count(char):
                return False
        return True
