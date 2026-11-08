class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        la = -2147483649
        lb = -2147483649
        lc = -2147483649
        for i in range(len(nums)):
            if nums[i] == la or nums[i] == lb or nums[i] == lc:
                continue
            if la < nums[i]:
                lc = lb
                lb = la
                la = nums[i]
            elif nums[i] > lb:
                lc = lb
                lb = nums[i]
            elif nums[i] > lc:
                lc = nums[i]
        if lc == -2147483649:
            return la
        return lc