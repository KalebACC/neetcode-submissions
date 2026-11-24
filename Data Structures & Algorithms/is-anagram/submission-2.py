class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters1 = dict()
        letters2 = dict()

        if len(s) != len(t):
            return False

        for char in s:
            if char in letters1:
                letters1[char] = letters1[char] + 1
            else:
                letters1[char] = 1
        
        for char in t:
            if char in letters2:
                letters2[char] = letters2[char] + 1
            else:
                letters2[char] = 1
        
        return letters2 == letters1

            
