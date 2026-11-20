class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        ans,c = 0,1
        for i in range(len(nums)):
            ans += nums[i] * c
            c *= -1
        return ans