class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []

        for letter in s:

            #Check last letter in the stack
            if stk and stk[-1][0] == letter:
                stk[-1][1] += 1 # if letter is equal to last letter in stack incrememt
            else:
                stk.append([letter,1]) #add the letter to the stack
            
            if stk[-1][1] == k: #check for valid grouping and pop
                stk.pop()

        return "".join(letter * count for letter, count in stk)