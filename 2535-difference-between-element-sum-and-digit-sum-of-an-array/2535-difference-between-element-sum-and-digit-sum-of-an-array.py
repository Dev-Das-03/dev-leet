class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        es,ds = 0,0
        for i in range(len(nums)):
            es += nums[i]
            n = nums[i]
            while n > 0:
                ds += n % 10
                n //= 10
        return abs(es-ds)