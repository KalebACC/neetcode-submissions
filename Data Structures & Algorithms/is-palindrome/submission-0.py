class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        back = len(s)-1

        while front < back:
            a = s[front].lower()
            b = s[back].lower()

            if not a.isalnum():
                front += 1
                a = s[front].lower()
                continue
            
            elif not b.isalnum():
                back -= 1
                b = s[back].lower()
                continue

            elif (a != b):
                return False
            
            front +=1
            back -=1

        return True