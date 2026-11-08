class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        m = 0
        c = 0
        for i in range(len(nums)):
            if c == 0:
                m = nums[i]
                c += 1
            elif nums[i] == m:
                c += 1
            else:
                c -= 1
        return m