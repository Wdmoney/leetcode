# with convert int to string
# todo without convert to string

class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=str(x)
        if len(y) == 1:
            return True
        for i in range(len(y)//2):
            if y[i] != y[len(y)-i-1]:
                return False
        return True

myvar = Solution()
x = 101
print(myvar.isPalindrome(x))
x = 11111100111111
print(myvar.isPalindrome(x))
