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
# the best solution (the most important thing is the sorted(v))

    def longestCommonPrefix1(self, v: list) -> str:
        ans = ""
        v = sorted(v)
        first = v[0]
        last = v[-1]
        for i in range(min(len(first), len(last))):
            if(first[i] != last[i]):
                return ans
            ans += first[i]
        return ans


strs = ["flower", "flow", "flight"]
#strs = []
prefix = Solution()
print(prefix.longestCommonPrefix(strs))
