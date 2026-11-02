class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        res=len(nums)
        for i in range(0,len(nums)):
            res^=i^nums[i]
        return res    
        