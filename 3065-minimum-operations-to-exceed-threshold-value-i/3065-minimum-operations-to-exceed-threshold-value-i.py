class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        c = 0
        for i in range(len(nums)):
            if nums[i] < k:
                c += 1
        return c