class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        stillOk = True
        if len(strs) != 0:
            if len(strs[0]) != 0:
                pref = strs[0][0]
        else:
            return ""
        prefresult = ""
        i = 0
        while i < len(strs[0]) and stillOk:
            for word in strs:
                if len(word) >= i+1:
                    if word[0:i+1] != pref:
                        stillOk = False
                else:
                    stillOk = False
            if stillOk:
                i = i+1
                prefresult = pref
                pref = word[0:i+1]
        return prefresult


strs = ["flower", "flow", "flight"]
#strs = []
prefix = Solution()
print(prefix.longestCommonPrefix(strs))
