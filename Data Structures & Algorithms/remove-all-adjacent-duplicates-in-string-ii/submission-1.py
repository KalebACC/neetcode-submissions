class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []

        for letter in s:
            if stk and stk[-1][0] == letter:
                stk[-1][1] += 1
            else:
                stk.append([letter,1])
            
            if stk[-1][1] == k:
                stk.pop()

        return "".join(letter * count for letter, count in stk)