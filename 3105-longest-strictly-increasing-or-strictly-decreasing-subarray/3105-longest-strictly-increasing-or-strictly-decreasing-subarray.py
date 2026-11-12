class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        i,d,ans = 1,1,1
        for j in range(1,len(nums)):
            if nums[j-1] < nums[j]:
                i += 1
                d = 1
            elif nums[j-1] > nums[j]:
                d += 1
                i = 1
            else:
                i,d = 1,1
            ans = max(ans,i,d)
        return ans