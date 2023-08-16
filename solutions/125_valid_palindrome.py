import string


class Solution:
    def isPalindrome1(self, s: str) -> bool:
        sinput = []
        for lett in s.lower():
            if lett in string.ascii_lowercase:
                sinput.append(lett)
        isStillOk = True
        lenght = len(sinput) // 2
        i = 0
        while i <= lenght and isStillOk:
            if sinput[i] != sinput[-i]:
                isStillOk = False
            else:
                i += 1
        return isStillOk

    def isPalindrome2(self, s: str) -> bool:
        sinput = []
        for lett in s.lower():
            if lett in string.ascii_lowercase + string.digits:
                sinput.append(lett)
        for i in range(len(sinput) // 2):
            if sinput[i] != sinput[-i-1]:
                return False
        return True

# the best!!!!! (import string not nessecary. 1 loop)
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1
        while (end - start) >= 1:
            validsymb = False
            while not validsymb and (end - start) >= 1:
                if s[start].isalpha() or s[start].isdigit():
                    validsymb = True
                else:
                    start += 1
            validsymb = False
            while not validsymb and (end - start) >= 1:
                if s[end].isalpha() or s[end].isdigit():
                    validsymb = True
                else:
                    end -= 1
            print(s[start].lower() + s[end].lower())
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True


s = "A m#an, a plan, a c!an^al: Panama"
#s = "dhf gh dh dgj dfd ,sk dfmh^%&%^&56"
mystr = Solution()
print(mystr.isPalindrome(s))
