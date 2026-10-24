class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        c = 0
        k = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                k += 1
            else:
                if k > c:
                    c = k
                k = 0

        if k > c:
            c = k
            
        return c