class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        if nums[0] >= nums[-1]:
            for i in range(len(nums)-1):
                if nums[i] < nums[i+1]:
                    return False
            return True

        elif nums[0] <= nums[-1]:
            for j in range(len(nums)-1):
                if nums[j] > nums[j+1]:
                    return False
            return True

