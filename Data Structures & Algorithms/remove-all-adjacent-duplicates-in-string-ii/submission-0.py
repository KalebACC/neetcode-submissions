class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        for letter in s:
            if letter*k in s:
                s = s.replace(letter*k,"")
        return s