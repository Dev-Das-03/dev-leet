class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        n = len(nums) - 1
        while l <= n:
            m = (l + n) // 2
            if target == nums[m]:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                n = m - 1
        return -1