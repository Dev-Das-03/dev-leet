class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        ans = 0
        if len(nums) == 1:
            return nums[0]
        for i in range(1,len(nums),2):
            ans += nums[i]
        return sum(nums) - ans*2