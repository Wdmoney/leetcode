class Solution:    
    def twoSum1(self, nums: list[int], target: int) -> list[int]:
        i = 0
        found = False
        while i < len(nums) and not found:
            j= i+1
            while j < len(nums) and not found:
                if nums[i] + nums[j] == target:
                    found = True
                else:
                    j +=1
            if not found:
                i +=1
        if found:
            return [i,j]
        else:
            return[]

    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        dict = {}
        for i,n in enumerate(nums):
            #print(i,n)
            if n in dict:
                return [dict[n], i]
            dict[target - n] = i
        return []
myvar = Solution()

nums = [2,7,11,15]
target = 9

print(myvar.twoSum1(nums, target))
print(myvar.twoSum2(nums, target))
